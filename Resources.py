assessment_score = 85
location = "Poland"
location2 = "Canada"
location3 = "US"

if (location3 == "US" or location2 == "Canada") and assessment_score >= 75:
  print(f"Your assessment score is {assessment_score}/100! You're hired!")
elif location == "US" and location != "Canada" and assessment_score >= 75:
  print(f"Apologies, you are based in {location} but this role requires you to be based in the US/Canada. Would you be interested in another role?")
elif location == "Poland" and assessment_score >= 75:
  print("Jest dobrze")
else:
  print(f"Thank you for your interest, we regret to inform you that we will not be moving forward with your application.")