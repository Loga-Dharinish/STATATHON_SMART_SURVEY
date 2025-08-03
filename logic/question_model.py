
def get_next_question(last_q, ans):
    if last_q == "Q1":
        return {"id": "Q2", "text": "Are you a student?" if int(ans) < 18 else "Are you employed?"}
    if last_q == "Q2" and ans.lower() == "yes":
        return {"id": "Q3", "text": "Which class are you studying?"}
    if last_q == "Q2" and ans.lower() == "no":
        return {"id": "Q4", "text": "Do you plan to continue your education?"}
    return {"id": "END", "text": "✅ Thank you for completing the survey!"}
