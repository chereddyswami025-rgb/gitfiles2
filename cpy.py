Hello team,
        swami@gmail.com
Please contact john.doe@example.com for project updates.
Also loop in jane_doe+alerts@sub.mail-example.co.uk and admin@EXAMPLE.COM.
For billing, use billing@finance.example.org or accounts-payable@corp.example-company.com.
Temporary contact: temp.user123@mail.example.in
Spam test: spammy+offers@promos.example.com, spammy+offers@promos.example.com

Customer list:
- Alice <alice.smith@example.com>
- Bob (bob_the.builder99@construction-example.net)
- Carol: carol.o'reilly@examplesite.org
- Dave: dave@localhost
- Eve: eve@@broken.email
- Frank: frank.email@.missingdomain
- Grace: grace@sub.subdomain.example.co
- Henry: HENRY.UPPERCASE@EXAMPLE.COM

Random inline: reach.me(at)example(dot)com or reach.me@example[dot]com — these are obfuscated.

CSV row:
"Name","Email"
"Sam","sam.surname+tag@my-mail.example"
"Uma","uma.k@short.io"

HTML snippet:
<a href="mailto:webmaster@example.com">Contact</a>
<img alt="admin" data-email="admin-contact@example-service.com">

Notes:
- test.user@verylongtld.technology
- duplicate@example.com
- duplicate@example.com

Edge cases to test:
- quoted: "quoted.name"@example.com
- numeric TLD? user@domain.123 (invalid for most regexes)
- trailing punctuation: mark@domain.com, end.
- parentheses (note): (paren_email@notes.example)

End of file.