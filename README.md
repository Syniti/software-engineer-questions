# Software Engineer

Hello, and welcome from the Syniti Engineering Team!

Thank you for your interest in joining Syniti, we're working on some
interesting and challenging problems and are looking for engineers with a
growth mindset to join our team. Our interview process helps us learn about
you as a person and at a technical level. But it's just as important that you
learn about us, our work, and our expectations so you know what you're
getting into. We foster a work environment where we are all comfortable and
love coming to work each day. We don't hire lightly and expect everyone to
contribute on day one.

Let's get started!

Please clone or download this repo and use it for the exercises described below.
Once completed you may either send us the URL to your git repo or a zip of
the folder.

We have four questions that we like to ask to get a sense of who you are, 
followed by a coding question we use to understand your technical strengths. 
You can write your responses to the first four questions directly in the README 
or as a separate file.

In answering the code question, please submit code as if you intended to
ship it to production. The details matter. Tests are expected, as is
well-written, simple, idiomatic code. While there are many libraries you
could use, we're expecting to mostly see code that you write yourself. Please
only use critical libraries for common functionality, such as parsing JSON or
writing tests.

We'd recommend you use whatever language you feel strongest in. It doesn't have
to be one we use (mostly Go and JavaScript) — we believe good engineers can be 
productive in any language.

Here are the questions, good luck!

1. What’s your proudest achievement? It can be a personal project or something
   you’ve worked on professionally. Just a short paragraph is fine, but I’d
   love to know why you’re proud of it.

Ans : The proudest achievement for me is bulding my own project (Coeus) from scratch in golang, back when I was working in a non-techincal job, I have no idea about Golang or API building or anything. I took up the challenge to learn Golang and started creating a webapp which helps students to test their skills in their specific subject of interest. I'm the full stack developer for that project. For me that is the proudest achievement because it made me realize how fast learner and dedicated worker I am.

2. What's a personal project you're currently working on? This could be a
   coding side project, hobby, or otherwise real world project you're working
   on.

Ans: No, Nothing right now.

3. Tell us about a technical book or article you read recently, why you liked
   it, and why we should read it.

 Ans : I recently read about Edge Computing which talks about reducing the processing time and latency and bandwidth issues with cloud computing by processing some of the simple transactions or tasks at the local level by using the systems hardware and not hitting cloud for every small transaction. It enhances the way AI work in the future as AI algorithms involves more processing at faster rates. I particularly liked the idea of using the local resources or installing small hardware to the local devices for the operations rather than using cloud for every transaction.

4. Tell us about one of your favorite products (physical or software) and one
   specific aspect that makes it truly great.

Ans : My answer to this is Tesla cars - it is one of the greatest innovation a person can imagine,self driving cars. which makes use of sensors all around the car to decide the right path and speed to drive, it looks easier on the outside but it involves many complex algorithms working under the hood which makes it truly great.

5. In this repo is a `data.json` file. It contains an imaginary example set
   of data a customer might need to migrate from one system to another. It's a
   JSON encoded array of objects. The customer understands some of the data
   might be bad and wants to know which records are invalid so they can ensure
   the new system will only have valid data. Write a program that will read
   in the data and mark any records:

   1. That are a duplicate of another record
   2. `name` field is null, missing, or blank
   3. `address` field is null, missing, or blank
   4. `zip` is null, missing, or an invalid U.S. zipcode

   Each record has an ID but that should only be used to identify a record,
   not for validity or duplication testing (eg, two records may be identical
   but have different IDs).

The output of the program should list the IDs of each invalid or duplicate
record, one per line. In the case of duplicates, mark both.

Example:

```
123ba
439a2
99abc
bac34
```

If you have any questions about the coding questions, please let us know.
