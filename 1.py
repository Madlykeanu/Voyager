from voyager import Voyager

# You can also use mc_port instead of azure_login, but azure_login is highly recommended

openai_api_key = "YOUR_API_KEY"

voyager = Voyager(
    mc_port=53988,
    openai_api_key=openai_api_key,
)

# start lifelong learning
voyager.learn()