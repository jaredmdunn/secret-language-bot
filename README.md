# secret-language-bot
A Twitter bot that encrypts @s into a "secret language" (e.g. Pig Latin)
Check it out at [@secretlangbot](https://twitter.com/secretlangbot)!

## Current Features
Mention @secretlangbot and it will reply to your tweet by translating your tweet into a randomly selected "secret language".

If you provide a hashtag of one our languages, it will use that specific language.

### Languages

#### Pig Latin (#piglatin)

The rules to Pig Latin are simple:
1. If the word starts with a vowel, the Pig Latin version is the word with "yay" added on to the end (e.g., "almond" to "almonday").
2. If the word starts with a consonant, then the Pig Latin version is the word with the consonants removed from the front and appended the back along with "ay" (e.g., "peanut" to "eanutpay"). 

#### Caesar Cipher (#caesar)

The [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is a classic cipher where each letter is substituted for another letter according to a shift parameter.

## Features To Add
- [ ] Randomly choosing a shift parameter for the Caesar Cipher and allowing users to indicate the shift parameter that they want.
- [ ] Eggy Peggy - A secret language where "egg" is added before the vowels of each syllable in a word.
- [ ] Other languages and ciphers.
- [ ] Direct messaging.