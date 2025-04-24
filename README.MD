# Slack App Review Bot

## Installing Requirements
- Python 3.x
- Add venv (recommended): `python3 -m venv venv`
- `source venv/bin/activate`
- Required dependencies (install via `pip`):
  ```bash
  pip install -r requirements.txt
  ```

## Creating the Slack App

1. Create or login to your slack workspace.
2. Go to https://api.slack.com/apps
3. Create an app from manifest. Add this YAML:

```yaml
display_information:
  name: Playstore Review Bot

settings:
  org_deploy_enabled: false
  socket_mode_enabled: false
  is_hosted: false
  token_rotation_enabled: false
```


4. Go to incoming webhooks. Enable them.
5. Add new webhook to workspace. Add it to the channel you want.
6. Test with CURL and see if the bot input a message

```bash
curl -X POST -H 'Content-type: application/json' \
--data '{"text":"Hello, World!"}' https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

Note - Keep your slack webhook URL secret. Access to this URL allows write access to your slack channel.