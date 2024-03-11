# %%
import json
from openai import OpenAI
import os 

from utils import get_response_from_jailbreak, is_harmful

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

client = OpenAI()

with open('jailbreaks.json') as f:
  jailbreaks = json.load(f)

jail_num = 5

harmful_jailbreaks = {}
non_harmful_jailbreaks = {}
num_harmful = 0

for i in range(1,100):

  jail_break_prompt = jailbreaks[str(i)]
  # print('----------------')
  # print('PROMPT: ', jail_break_prompt)
  # print('----------------')

  response = get_response_from_jailbreak(jail_break_prompt)

  print('----------------')
  print('RESPONSE: ', response)
  print('----------------')


  is_flagged = is_harmful(response)

  print('IS HARMFUL: ', is_flagged)
  print('----------------')

  if is_flagged == 'True':
    harmful_jailbreaks[jail_break_prompt] = response

  elif is_flagged == 'False':
    non_harmful_jailbreaks[jail_break_prompt] = response
  
  else:
    print('ERROR: ', is_flagged)
    print('----------------')
  
  num_harmful += 1 if is_flagged == 'True' else 0


# %%

print(num_harmful)


for i in harmful_jailbreaks.values():
  print('-------------------------------------------------')
  print(i)
# %%


for i in non_harmful_jailbreaks.values():
  print('-------------------------------------------------')
  print(i)

# %%
