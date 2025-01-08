# Gemini API reading videos
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyAIGf_2RGsLijy4HAn60AvPMSPqN9Bf_Ic")  # configures my api key so that any call uses my api key
model = genai.GenerativeModel("gemini-1.5-flash")   # choses the model of Gemini

video_path = '/Users/suhaassurapaneni/Downloads/HomeSafe.mp4'
video_file = genai.upload_file(path=video_path)
print(f"Completed upload: {video_file.uri}")


#print(video_file.state.name)
# Check whether the file is ready to be used.
while video_file.state.name == "PROCESSING":
    print('.', end='')
    #time.sleep(10)
    video_file = genai.get_file(video_file.name)
print()

if video_file.state.name == "FAILED":
  raise ValueError(video_file.state.name)

# Create the prompt.
prompt = "Summarize this video."

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# Make the LLM request.
print("Making LLM inference request...")
response = model.generate_content([video_file, prompt],
                                  request_options={"timeout": 600})

# Print the response, rendering any Markdown
print(response.text)