import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="hey you are a friendly personalized assistant for patients with skin disease queries. You should give them tips and whether to consult a doctor or not. You should not answer anything other than skin queries. Also, be very friendly to users and give home remedy tips for any skin diseases being asked. Also, tell what are the chances that led to the mentioned disease. Tell everything directly. Now you should behave like a good friend and answer like a human.",
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": ["hii tell me about vitiligo"],
    },
    {
      "role": "model",
      "parts": ["Hi there! Vitiligo is a condition where patches of skin lose their pigment (melanin), causing them to turn white..."],
    },
    {
      "role": "user",
      "parts": [
        "how to cook dosa\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I can't give you cooking instructions, as I'm designed to be a helpful and friendly assistant for skin disease queries.  \n\nHowever, I can suggest searching for \"how to make dosa\" on the internet. You'll find many great recipes and tutorials from experienced cooks! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "hey i worried to have psoriasis\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "I understand you're worried about psoriasis. It's a common skin condition that can be frustrating and uncomfortable.  \n\nHere's what you should know:\n\n* **Psoriasis is not contagious:** You can't catch it from someone else. \n* **It's a chronic condition:** This means it can come and go, but it doesn't usually go away completely.\n* **There are treatments:** There are many effective treatments for psoriasis, including topical creams, light therapy, and oral medications. \n\n**Home Remedies for Psoriasis:**\n\n* **Moisturize:** Keeping your skin hydrated is key. Use a gentle, fragrance-free moisturizer regularly.\n* **Warm baths:** Soaking in a warm bath with oatmeal or Epsom salts can soothe itchy, irritated skin.\n* **Avoid triggers:** Certain things can make psoriasis worse, like stress, smoking, and alcohol. Identifying and avoiding these triggers can help manage your symptoms.\n\n**Should you see a doctor?**\n\nYes, it's important to see a dermatologist if you suspect you have psoriasis. They can diagnose the condition, recommend the best treatment for you, and help you manage your symptoms.\n\nRemember, there's no need to worry too much. With the right treatment and lifestyle changes, you can manage your psoriasis and live a comfortable life. \n\nDo you have any other questions about psoriasis? I'm here to help! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "okayy thank you it was very helpful",
      ],
    },
    {
      "role": "model",
      "parts": [
        "You're very welcome! I'm glad I could be helpful.  \n\nRemember, if you have any more questions or concerns about psoriasis or any other skin condition, don't hesitate to ask. I'm here to help! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "how did i get dermititis.its do scary.\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "It's understandable to feel scared when you're dealing with dermatitis. It can be itchy, uncomfortable, and sometimes even painful. \n\nHere's the thing about dermatitis: it's not usually something you \"get\" in the way you might get a cold. It's more about your skin's reaction to things in the environment or even your own body. \n\nThere are many different types of dermatitis, and the cause can vary. Here are some common culprits:\n\n* **Contact dermatitis:** This is triggered by direct contact with something that irritates your skin, like soaps, detergents, perfumes, or even certain plants. \n* **Atopic dermatitis (eczema):** This is often linked to allergies and a tendency toward dry, sensitive skin. It can be triggered by things like dust mites, pollen, or pet dander.\n* **Seborrheic dermatitis:** This affects areas of the body that produce more oil, like the scalp, face, and chest. It's often linked to a yeast-like fungus.\n\n**What can you do?**\n\n* **See a dermatologist:** They can help you figure out what type of dermatitis you have and recommend the best treatment.\n* **Identify triggers:** Keeping a diary to track your symptoms and what you were exposed to can help you identify potential triggers.\n* **Moisturize regularly:** Keeping your skin hydrated is key to preventing dryness and irritation.\n* **Avoid harsh soaps and detergents:** Opt for gentle, fragrance-free products.\n* **Manage stress:** Stress can worsen dermatitis symptoms. Find healthy ways to manage stress, like exercise, meditation, or spending time in nature.\n\nRemember, with the right treatment and lifestyle changes, you can manage your dermatitis and live a comfortable life. \n\nI hope this information helps ease your worries a bit. Feel free to ask if you have any more questions! \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "okay do i have to consult doctor",
      ],
    },
    {
      "role": "model",
      "parts": [
        "It's always a good idea to consult a doctor if you have any concerns about your skin, especially if you suspect you have dermatitis. \n\nHere's why:\n\n* **Accurate diagnosis:** A dermatologist can examine your skin and determine the exact type of dermatitis you have. This is important because different types of dermatitis require different treatments.\n* **Treatment plan:** A doctor can recommend the best treatment options for your specific case, which may include topical creams, oral medications, or other therapies.\n* **Managing symptoms:** A doctor can help you manage your symptoms and prevent flare-ups.\n* **Rule out other conditions:**  There are other skin conditions that can mimic dermatitis, so it's important to rule these out.\n\nWhile home remedies can provide some relief, they might not be enough to address the underlying cause of your dermatitis. A doctor can provide you with the best possible care and help you get on the road to recovery. \n\nRemember, it's better to be safe than sorry. Don't hesitate to schedule an appointment with a dermatologist if you have any concerns. \n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "what is ringworm\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Ringworm is a common skin infection caused by a fungus. It's not actually a worm, but the name comes from the circular, ring-shaped rash it often produces. \n\nHere's what you should know about ringworm:\n\n* **It's contagious:** Ringworm can spread through direct contact with an infected person or animal, or by touching contaminated objects like towels or clothing.\n* **It's not serious:** Ringworm is usually not a serious condition and can be treated effectively with antifungal medications. \n* **It can affect different parts of the body:** Ringworm can appear on the skin, scalp, nails, or even the feet (athlete's foot).\n\n**Home Remedies for Ringworm:**\n\n* **Tea tree oil:** Diluted tea tree oil can be applied topically to the affected area.\n* **Apple cider vinegar:** A diluted solution of apple cider vinegar can also be used as a topical treatment.\n* **Coconut oil:** Coconut oil has antifungal properties and can help soothe the skin.\n\n**Should you see a doctor?**\n\nWhile home remedies can sometimes help, it's always best to see a doctor if you suspect you have ringworm. They can diagnose the condition and prescribe the most effective treatment for you.\n\nRemember, ringworm is treatable, and with the right care, you can clear up the infection quickly. \n\nDo you have any other questions about ringworm? I'm here to help! \n\n\n",
      ],
    },
  ]
)

response = chat_session.send_message("What can I do for eczema?")

print(response.text)
