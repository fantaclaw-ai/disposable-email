# disposable-email

An OpenClaw AgentSkill for creating disposable Mail.tm inboxes and extracting OTP codes programmatically.

## Purpose

Helps OpenClaw agents create temporary email addresses, poll for incoming messages, and extract one-time passwords (OTPs) for email verification testing.

## Features

- **Disposable Inboxes**: Create Mail.tm temporary email addresses instantly
- **Message Polling**: List and read incoming emails
- **OTP Extraction**: Automatically detect and extract OTP codes from emails
- **End-to-End Flow**: Create inbox, wait for email, extract OTP in one command
- **No Dependencies**: Pure Python with stdlib only (no pip install needed)

## Installation

```bash
npx clawhub@latest install disposable-email
```

## Usage

Once installed, OpenClaw will automatically use this skill when you mention:
- "Create a temporary email"
- "Generate a temp inbox"
- "I need a disposable email address"
- "Extract the OTP from this email"
- "Wait for a verification code"

### Quick Start

**Create a disposable inbox:**
```bash
python3 scripts/create_inbox.py
# Output: {"address": "amber.cloud.1234@mail.tm", "token": "...", ...}
```

**List messages:**
```bash
python3 scripts/read_inbox.py --token <TOKEN> --list
```

**Wait for OTP:**
```bash
python3 scripts/read_inbox.py --token <TOKEN> --wait-otp --timeout 120
# Output: {"otp": "123456", "message": {...}}
```

**End-to-end (create + wait for OTP):**
```bash
python3 scripts/e2e_otp.py --timeout 120
# First emits inbox_created, then otp_found/message_received_no_otp/timeout
```

## Files

```
disposable-email/
├── README.md           # This file (repo documentation)
├── LICENSE             # MIT License
├── SKILL.md            # Main skill instructions
└── scripts/
    ├── create_inbox.py # Create a new Mail.tm inbox
    ├── read_inbox.py   # Read messages and extract OTPs
    └── e2e_otp.py      # End-to-end OTP extraction flow
```

## Limitations

- Free Mail.tm domains may be blocked by some production services
- Temporary emails are not suitable for long-term use
- Token should be treated as mailbox credentials (keep private)

## License

MIT

## Links

- [Mail.tm](https://mail.tm) - Temporary email service
- [ClawHub](https://clawhub.ai) - Skill marketplace