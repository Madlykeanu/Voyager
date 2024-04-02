from voyager import Voyager

# You can also use mc_port instead of azure_login, but azure_login is highly recommended

openai_api_key = "YOUR_API_KEY"

voyager = Voyager(
    mc_port=25565,
    openai_api_key=openai_api_key,
    env_request_timeout=1200,
    # skill_library_dir="./skill_library/trial1", # Load a learned skill library.
)

# start lifelong learning
voyager.learn()