import os
import requests
import json
import random
import re
import gradio as gr

def img_detector(model, url):
    api_keys = [
        os.getenv("OPENROUTER_API_KEY_1"),
        os.getenv("OPENROUTER_API_KEY_2"),
        os.getenv("OPENROUTER_API_KEY_3"),
        os.getenv("OPENROUTER_API_KEY_4"),
    ]
    api_keys = [k for k in api_keys if k]
    errors = []
    for api_key in api_keys:
        try:
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
                data=json.dumps({
                    "model": model,
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "What is appear in this image? Please provide a detailed description."},
                                {"type": "image_url", "image_url": {"url": url}}
                            ]
                        }
                    ]
                })
            )
            if response.status_code == 200:
                data = response.json()
                if 'choices' in data and len(data['choices']) > 0:
                    return data['choices'][0]['message']['content']
                else:
                    errors.append(f"API key {api_key[:8]}...: No choices in response.")
            else:
                errors.append(f"API key {api_key[:8]}...: Status {response.status_code}")
        except Exception as e:
            errors.append(f"API key {api_key[:8]}...: Exception {e}")
    return f"All VLM API requests failed: {' | '.join(errors)}"

def evaluate_written_english(vlm_description, written_input, lang="english"):
    """
    Evaluate written English based on a VLM image description and a written paragraph.
    Returns a dict with feedback and scores.
    """
    DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
    if not DEEPSEEK_API_KEY:
        raise EnvironmentError("Missing DEEPSEEK_API_KEY in environment.")

    prompt = f"""
    You are an expert English writing tutor following the CEFR framework (A1-C2) to help learners improve their writing based on images and their written paragraphs.

    The learner was shown the following image (described by a vision-language model):
    ---
    {vlm_description}
    ---

    Then the learner wrote the following paragraph in English:
    ---
    {written_input}
    ---

    Please provide a JSON response that includes:
    1. "relevance_score": A score out of 100 evaluating how relevant the paragraph is to the image.
    2. "grammar_score": A score out of 100 evaluating grammar accuracy (subject-verb agreement, tense, etc.).
    3. "vocabulary_score": A score out of 100 evaluating the richness and accuracy of vocabulary.
    4. "mistakes": A list of grammar or vocabulary mistakes with suggestions for improvement.
    5. "corrections": A corrected and polished version of the paragraph.
    6. "learning_level": The estimated CEFR level (A1 to C2).
    7. "tips": Actionable tips to improve writing based on the mistakes.
    8. "highlight": A positive observation about the learner's writing (e.g. a strong sentence, clever word use).
    9. "motivational_comment": A short, warm, encouraging comment to motivate the learner.

    Format the response as clean JSON.
    """

    try:
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {DEEPSEEK_API_KEY}"},
            json={
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a certified English writing tutor helping students improve grammar, vocabulary, and structure. You give feedback using CEFR standards and encourage learners with kind human messages."
                    },
                    {
                        "role": "user",
                        "content": prompt.strip()
                    }
                ],
                "temperature": random.uniform(0.9, 1),
                "max_tokens": 1500
            }
        )

        if response.status_code == 200:
            data = response.json()
            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0]["message"]["content"]
                clean_json_text = re.sub(r"```json|```", "", content).strip()

                try:
                    return json.loads(clean_json_text)
                except json.JSONDecodeError as decode_err:
                    return {
                        "relevance_score": 0,
                        "grammar_score": 0,
                        "vocabulary_score": 0,
                        "mistakes": [],
                        "corrections": "N/A",
                        "learning_level": "Unknown",
                        "highlight": "N/A",
                        "motivational_comment": "N/A",
                        "tips": [f"Invalid JSON format: {str(decode_err)}", "Raw content:", clean_json_text]
                    }
        else:
            return {
                "relevance_score": 0,
                "grammar_score": 0,
                "vocabulary_score": 0,
                "mistakes": [],
                "corrections": "N/A",
                "learning_level": "Unknown",
                "highlight": "N/A",
                "motivational_comment": "N/A",
                "tips": [f"API Error: {response.status_code}"]
            }

    except Exception as e:
        return {
            "relevance_score": 0,
            "grammar_score": 0,
            "vocabulary_score": 0,
            "mistakes": [],
            "corrections": "N/A",
            "learning_level": "Unknown",
            "highlight": "N/A",
            "motivational_comment": "N/A",
            "tips": [f"Exception occurred: {str(e)}"]
        }

def gradio_written_eval(image_url, paragraph, model="meta-llama/llama-3.2-11b-vision-instruct:free"):
    vlm_desc = img_detector(model, image_url)
    result = evaluate_written_english(vlm_desc, paragraph)
    return json.dumps(result, indent=2, ensure_ascii=False)

iface = gr.Interface(
    fn=gradio_written_eval,
    inputs=[
        gr.Textbox(label="Image URL"),
        gr.Textbox(label="Your Paragraph", lines=6),
        gr.Dropdown(choices=["meta-llama/llama-3.2-11b-vision-instruct:free", "google/gemini-2.0-flash-exp:free"], value="meta-llama/llama-3.2-11b-vision-instruct:free", label="Vision Model")
    ],
    outputs=gr.Code(label="Evaluation JSON", language="json"),
    title="Written English Evaluation",
    description="Paste an image URL and your paragraph describing the image. The system will analyze your writing and return a detailed evaluation."
)

if __name__ == "__main__":
    iface.launch()
