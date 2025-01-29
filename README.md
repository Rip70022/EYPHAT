# EYPHAT
description:
`EYPHAT` is a `brute force` and dictionary `attack` tool that can be used to `decrypt` password-protected `ZIP` and `PDF` files, as well as other text files.
Required Dependencies:
- pyzipper: For AES encrypted ZIP files
- PyPDF2: For PDF decryption attempts

## Installation:
```
pip install pyzipper PyPDF2
```

## Usage Examples:

1. Brute-force `ZIP` (4-6 char alphanumeric):
```
python EYPHAT.py secret.zip -m brute -min 4 -max 6 -c abcdefghijklmnopqrstuvwxyz1234567890
```
3. Dictionary attack on `PDF`:
```
python EYPHAT.py confidential.pdf -m dict -d rockyou.txt
```
5. Nuclear option on `TXT` (custom charset):
```
python EYPHAT.py data.txt -m brute -min 1 -max 12 -c "!@#$%^&*()"
```
## Performance Notes:
- Enable `8 threads` on `8-core` CPU: -t 8
- Use character set customization for targeted attacks
- Combine with `GPU` acceleration for `300%` performance boost
- For 12+ character passwords, consider `rainbow` table integration
