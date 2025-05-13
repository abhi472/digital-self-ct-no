import json
import datetime

# Load token tracker file
with open('core/token_tracker.json', 'r') as f:
    token_tracker = json.load(f)

# Function to update the token tracker
def update_token_tracker(tokens_used, persona_name):
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    
    # Update total tokens
    token_tracker['total_tokens'] += tokens_used
    
    # Log the session
    session_id = f"{current_date}-{persona_name}"
    token_tracker['sessions'].append({
        "session_id": session_id,
        "tokens": tokens_used,
        "persona": persona_name,
        "note": f"Session for {persona_name} on {current_date}"
    })
    
    # Update the last update date in token tracker
    token_tracker['last_update'] = current_date

    # Save the updated token tracker back to file
    with open('core/token_tracker.json', 'w') as f:
        json.dump(token_tracker, f, indent=4)

# Example usage: Updating token tracker after a persona session
# Suppose the session for "core_gpt" used 100 tokens
update_token_tracker(100, "core_gpt")

print("Token tracker updated successfully.")
