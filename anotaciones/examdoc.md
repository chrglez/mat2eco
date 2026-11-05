|     |     | Using | the        | exam      | document       | class |     |     |
| --- | --- | ----- | ---------- | --------- | -------------- | ----- | --- | --- |
|     |     |       | Philip     |           | Hirschhorn     |       |     |     |
|     |     |       | Department |           | of Mathematics |       |     |     |
|     |     |       |            | Wellesley | College        |       |     |     |
|     |     |       | Wellesley, |           | MA 02481       |       |     |     |
psh@math.mit.edu
©
Copyright 1994, 1997, 2000, 2004, 2008, 2011, 2015, 2017, 2021, 2023
|     |      |               | Philip |             | Hirschhorn |                   |        |     |
| --- | ---- | ------------- | ------ | ----------- | ---------- | ----------------- | ------ | --- |
|     |      |               | All    | rights      | reserved   |                   |        |     |
|     |      |               |        | July        | 9, 2023    |                   |        |     |
|     | This | is the user’s | guide  | for version | 2.704 of   | the exam document | class. |     |
Contents
| 1 Introduction |     |     |     |     |     |     |     | 4   |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1.1 License . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
| 2 Simple | instructions | for | a basic | exam |     |     |     | 6   |
| -------- | ------------ | --- | ------- | ---- | --- | --- | --- | --- |
2.1 The \documentclass command . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Asking for the student’s name . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.3 Asking questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.4 Questions with parts, and subparts, and subsubparts . . . . . . . . . . . . . 8
2.5 Leaving space for the answers . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.6 Headers and footers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
| 3 The |     | command |     |     |     |     |     | 11  |
| ----- | --- | ------- | --- | --- | --- | --- | --- | --- |
\documentclass
3.1 The option addpoints . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2 The option answers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
| 4 Questions | and | points |     |     |     |     |     | 13  |
| ----------- | --- | ------ | --- | --- | --- | --- | --- | --- |
4.1 Questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
4.2 Questions with parts and subparts (and subsubparts) . . . . . . . . . . . . . 14
4.3 Point values for the questions . . . . . . . . . . . . . . . . . . . . . . . . . . 18
1

4.3.1 Where the points will be printed . . . . . . . . . . . . . . . . . . . . 18
4.3.2 Printing the points at the end of the question . . . . . . . . . . . . . 20
4.3.3 Half points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
4.3.4 Surrounding the points: Parentheses, brackets, or a box . . . . . . . . 22
4.3.5 Using a substitute for the word “points” . . . . . . . . . . . . . . . . 24
4.3.6 Using \marginpointname and enlarging the margins . . . . . . . . . 26
4.3.7 Completely customizing the points . . . . . . . . . . . . . . . . . . . 26
4.3.8 Questions that begin with a parts environment . . . . . . . . . . . . . 28
4.3.9 Adding up the points for a question . . . . . . . . . . . . . . . . . . . 29
4.3.10 Margin sizes when using \pointsinmargin and \pointsinrightmargin 31
4.4 Custom question number lines: The \qformat command . . . . . . . . . . . 32
4.4.1 Adding up the points for a question . . . . . . . . . . . . . . . . . . . 33
4.5 Titled questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.5.1 \titledquestion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.5.2 \thequestiontitle . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.6 Bonus points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.7 Counting the questions and adding up the points . . . . . . . . . . . . . . . 37
4.8 Referring to specific questions by number (cross references) . . . . . . . . . . 38
4.9 Customizing the numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.10 Customizing the list parameters . . . . . . . . . . . . . . . . . . . . . . . . . 41
5 Multiple choice and fill in the blank questions 42
5.1 The choices environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.2 The oneparchoices environment . . . . . . . . . . . . . . . . . . . . . . . . 43
5.3 The checkboxes environment . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.4 The oneparcheckboxes environment . . . . . . . . . . . . . . . . . . . . . . 44
5.5 Solutions to multiple choice questions . . . . . . . . . . . . . . . . . . . . . . 45
5.6 Fill in the blank questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.6.1 True/False questions . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
5.6.2 Customizing the \fillin command . . . . . . . . . . . . . . . . . . . 47
5.7 Customizing the multiple choice environments . . . . . . . . . . . . . . . . . 48
6 Escaping the indentation: \uplevel and \fullwidth 50
6.1 Including instructions for a group of questions . . . . . . . . . . . . . . . . . 50
6.2 Naming the parts of a long exam . . . . . . . . . . . . . . . . . . . . . . . . 53
6.2.1 Using \uplevel and \fullwidth . . . . . . . . . . . . . . . . . . . . 54
6.2.2 Using the standard sectioning commands . . . . . . . . . . . . . . . . 55
7 Leaving space for the answers 55
7.1 Leaving blank space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.2 Printing an empty box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.3 Printing lined space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.4 Printing dotted lined space . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
7.5 Printing space filled with a grid . . . . . . . . . . . . . . . . . . . . . . . . . 62
Page 2

7.5.1 Covering every page with a grid . . . . . . . . . . . . . . . . . . . . . 64
7.5.2 Printing graph paper . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
7.6 Short answer questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
7.7 Printing the answers to short answer questions . . . . . . . . . . . . . . . . . 67
8 Solutions 68
8.1 Solution environments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
8.2 The appearance of the solution . . . . . . . . . . . . . . . . . . . . . . . . . 70
8.2.1 Printing the solution in a box . . . . . . . . . . . . . . . . . . . . . . 70
8.2.2 Printing the solution on a shaded background . . . . . . . . . . . . . 72
8.2.3 Printing the solution with no framing or shading . . . . . . . . . . . . 72
8.3 Imported graphics in solutions . . . . . . . . . . . . . . . . . . . . . . . . . . 73
8.4 Customizing the solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
8.4.1 The title . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
8.4.2 Solution emphasis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
8.4.3 Advanced customizations . . . . . . . . . . . . . . . . . . . . . . . . . 75
8.5 Leaving space for the answers when solutions aren’t printed . . . . . . . . . 75
8.5.1 Cancelling the space from the optional arguments . . . . . . . . . . . 77
8.6 The solutionbox environment . . . . . . . . . . . . . . . . . . . . . . . . . . 78
8.7 Solution box frames in color . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
8.8 Equations inside solutions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
8.9 Changes depending on whether or not solutions are being printed . . . . . . 80
8.9.1 Printing only selected solutions . . . . . . . . . . . . . . . . . . . . . 81
9 Grading tables and point tables 82
9.1 Grading tables indexed by question number or by page number . . . . . . . 82
9.1.1 Grading tables with multiple rows . . . . . . . . . . . . . . . . . . . . 85
9.1.2 Grading tables with multiple columns . . . . . . . . . . . . . . . . . . 86
9.2 Point tables indexed by question number or by page number . . . . . . . . . 87
9.2.1 Point tables with multiple rows . . . . . . . . . . . . . . . . . . . . . 89
9.2.2 Point tables with multiple columns . . . . . . . . . . . . . . . . . . . 90
9.3 Table entries as clickable links . . . . . . . . . . . . . . . . . . . . . . . . . . 91
9.4 Grading ranges, partial grading tables, and partial point tables . . . . . . . . 91
9.4.1 Partial grading tables and partial point tables with multiple rows . . 92
9.4.2 Partial grading tables and partial point tables with multiple columns 93
9.5 \pointsofquestion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
9.6 \pointsonpage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
9.7 Bonus grading tables and bonus point tables . . . . . . . . . . . . . . . . . . 95
9.8 Combined grading tables and combined point tables . . . . . . . . . . . . . . 96
9.9 Changing the total points in a table . . . . . . . . . . . . . . . . . . . . . . . 98
9.10 Customizing the tables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10 Changing the page margins 102
Page 3

11 Headers and footers 103
11.1 Page styles: Headers and/or footers . . . . . . . . . . . . . . . . . . . . . . . 103
11.2 The three parts of the header . . . . . . . . . . . . . . . . . . . . . . . . . . 104
11.2.1 Using \header, \firstpageheader and \runningheader . . . . . . . 104
11.2.2 Using \lhead, \chead and \rhead . . . . . . . . . . . . . . . . . . . 105
11.2.3 Commands with optional arguments . . . . . . . . . . . . . . . . . . 107
11.3 The three parts of the footer . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
11.3.1 Using \footer, \firstpagefooter and \runningfooter . . . . . . . 107
11.3.2 Using \lfoot, \cfoot, and \rfoot . . . . . . . . . . . . . . . . . . . 108
11.4 Leaving extra room for multiple line headers and footers . . . . . . . . . . . 108
11.5 Horizontal rules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
11.6 Listing the number of pages in the exam . . . . . . . . . . . . . . . . . . . . 111
11.7 Treating the last page differently . . . . . . . . . . . . . . . . . . . . . . . . 111
11.8 Treating odd and even numbered pages differently . . . . . . . . . . . . . . . 112
11.9 Questions that span multiple pages . . . . . . . . . . . . . . . . . . . . . . . 113
11.9.1 Questions continuing from the previous page . . . . . . . . . . . . . . 113
11.9.2 Questions that continue onto a later page . . . . . . . . . . . . . . . . 115
11.10Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
11.10.1Example: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
11.10.2Example: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
11.10.3Example: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
11.10.4Example: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
11.10.5Example: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
11.10.6Example: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
11.10.7Example: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
11.10.8Example: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
12 Cover pages 126
12.1 Headers and footers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
12.2 Listing the number of cover pages . . . . . . . . . . . . . . . . . . . . . . . . 127
Index 129
1 Introduction
The file exam.cls provides the exam document class, which attempts to make it easy for
even a LATEX novice to prepare exams. Specifically, exam.cls sets the page layout so that
there are one inch margins all around (no matter what size paper you’re using) and provides
commands that make it easy to format questions, create flexible headers and footers, change
the margins, and create grading tables. In more detail:
• The class will automatically format and number the questions, parts of questions,
subparts of parts, and subsubparts of subparts (see sections 4.1 and 4.2).
Page 4

•
You can include the point value of each question (or part, or subpart, or subsubpart),
with your choice of having the point values printed at the beginning of the text of the
question, opposite that in the left margin, opposite that in the right margin, or in the
| right margin | opposite | the end | of the question | (see section 4.3). |
| ------------ | -------- | ------- | --------------- | ------------------ |
• The class will add up the total points for each question (and all of its parts, subparts,
and subsubparts) and the total points on each page, and make those totals available
| in macros | (see sections | 4.3.9, | 9.5 and 9.6). |     |
| --------- | ------------- | ------ | ------------- | --- |
• You can have the class print a grading table, indexed either by question number or by
| page number | (see section | 9.1). |     |     |
| ----------- | ------------ | ----- | --- | --- |
•
You specify the header in three parts: One part to be left justified, one part to be
centered, and one part to be right justified, and one or all of these can be omitted (see
section 11.2).
•
The footer is also specified in three parts: Left justified, centered, and right justified
| (see section | 11.3). |     |     |     |
| ------------ | ------ | --- | --- | --- |
• The header and footer for the first page can be different from the ones used on other
| pages | (see sections | 11.2.1, 11.2.2, | 11.3.1, and 11.3.2). |     |
| ----- | ------------- | --------------- | -------------------- | --- |
• Both headers and footers can contain more than one line. To accommodate headers
and footers with several lines, simple commands are provided to enlarge the part of the
page devoted to the header and/or footer, and these commands can give one amount
of space on the first page and a different amount of space on all other pages (see
section 11.4).
• Macros are defined to enable you to state the total number of pages in the exam (see
section 11.6) and to change the header and/or footer that appears on the last page of
| the exam | (see section | 11.7). |     |     |
| -------- | ------------ | ------ | --- | --- |
• Macros are defined so that the headers and footers can vary depending on whether
the current page begins a new question or continues a question that started on an
earlier page (and, if one continues onto the current page, to say what the number of
that question is). Macros are also defined so that the headers and footers can vary
depending on whether a question is complete on the current page or continues on to
the next page (and, if one continues, to say what the number of that question is) (see
section 11.9).
• You can have a horizontal rule at the base of the header and/or at the top of the footer
| (see section | 11.5). |     |     |     |
| ------------ | ------ | --- | --- | --- |
• The exam can begin with one or more cover pages, which are numbered separately
from the main pages of the exam and which can have headers and footers different
| from the | ones in the | main pages | of the exam (see | section 12). |
| -------- | ----------- | ---------- | ---------------- | ------------ |
Page 5

• You can include solutions in your LATEX file and have these solutions either printed
or ignored (or replaced automatically by space in which the students can write their
answers) depending on a single command (see section 8, section 5.5, and section 7.7).
The latest version of exam.cls (possibly a beta test version) should always be available
at http://www-math.mit.edu/~psh/.
1.1 License
• This work may be distributed and/or modified under the conditions of the LATEX
ProjectPublicLicense,eitherversion1.3ofthislicenseor(atyouroption)anylaterver-
sion. Thelatestversionofthislicenseisinhttp://www.latex-project.org/lppl.txt
and version 1.3 or later is part of all distributions of LATEX version 2003/12/01 or later.
• This work has the LPPL maintenance status “author-maintained”.
• This work consists of the files exam.cls and examdoc.tex.
2 Simple instructions for a basic exam
Producing a basic exam with the exam document class is fairly easy. After you learn to do
that, you can read the parts of this user’s guide that describe how to customize whatever
you want to change.
2.1 The \documentclass command
To use the exam document class, your \documentclass command should be
\documentclass[addpoints]{exam}
or, if you want to use 12 point type,
\documentclass[addpoints,12pt]{exam}
There are other options; for the full story, see section 3.
2.2 Asking for the student’s name
If you’ll be leaving space for the answers on the question pages (see sections 2.5 and 7), then
you’ll probably also want to leave space for the student’s name. If you type
\begin{center}
\fbox{\fbox{\parbox{5.5in}{\centering
Answer the questions in the spaces provided on the
question sheets. If you run out of room for an answer,
continue on the back of the page.}}}
Page 6

\end{center}
\vspace{0.1in}
| \makebox[\textwidth]{Name |     | and | section:\enspace\hrulefill} |     |     |
| ------------------------- | --- | --- | --------------------------- | --- | --- |
\vspace{0.2in}
| \makebox[\textwidth]{Instructor’s |     |     | name:\enspace\hrulefill} |     |     |
| --------------------------------- | --- | --- | ------------------------ | --- | --- |
after the \begin{document} command and before the \begin{questions} command (see
| section 4.1), | then you’ll | get |     |     |     |
| ------------- | ----------- | --- | --- | --- | --- |
Answer the questions in the spaces provided on the question sheets. If you
|              | run out   | of room for | an answer, continue | on the back | of the page. |
| ------------ | --------- | ----------- | ------------------- | ----------- | ------------ |
| Name and     | section:  |             |                     |             |              |
| Instructor’s | name:     |             |                     |             |              |
| 2.3 Asking   | questions |             |                     |             |              |
Once you’ve typed and (if the students will be writing their answers on
\begin{document}
the question pages) asked for the student’s name (see section 2.2), you can list the questions
on the exam in a questions environment. You begin each question with a \question
command, which is optionally followed by a number of points inside of square brackets. For
| example, | if you type |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- |
\begin{questions}
\question[10]
| Why is there | air? |     |     |     |     |
| ------------ | ---- | --- | --- | --- | --- |
\question[15]
How much wood would a woodchuck chuck if a woodchuck could chuck
wood?
| \question[10] | Compute | $\displaystyle\int_0^1 |     | x^2 \, dx$. |     |
| ------------- | ------- | ---------------------- | --- | ----------- | --- |
\end{questions}
| then you’ll    | get |               |        |     |     |
| -------------- | --- | ------------- | ------ | --- | --- |
| 1. (10 points) | Why | is there air? |        |     |     |
|                |     |               | Page 7 |     |     |

2. (15 points) How much wood would a woodchuck chuck if a woodchuck could chuck
wood?
(cid:90) 1
3. (10 points) Compute x2dx.
0
As the above example illustrates, you can leave blank lines between the \question com-
mand and the actual beginning of the question, or before the first \question command in
the environment, and they will be ignored. The point values are entirely optional; if you
omit the point values, you should also omit the square brackets containing them.
If you give the command \marksnotpoints, then the words “point” and “points” will be
replaced by the words “mark” and “marks”. There are many other customizations possible
for the points, including using a different language, changing the way the points are printed,
and by having them printed in one of the margins. For the full story, see section 4.3.
2.4 Questions with parts, and subparts, and subsubparts
Ifyouwanttocreateaquestionwithparts, youuseapartsenvironmentandbegineachpart
with the command \part. The parts environment can be at the beginning of a question
or after some text that begins the question. (There are also subparts and subsubparts
environments; for the full details, see section 4.2.) For example, if you type
\begin{questions}
\question[10]
Why is there air?
\question
What if there were no air?
\begin{parts}
\part[5]
Describe the effect on the balloon industry.
\part[5]
Describe the effect on the aircraft industry.
\end{parts}
\question[20]
\begin{parts}
\part
Define the universe. Give three examples.
\part
Page 8

If the universe were to end, how would you know?
\end{parts}
\end{questions}
then you’ll get
1. (10 points) Why is there air?
2. What if there were no air?
(a) (5 points) Describe the effect on the balloon industry.
(b) (5 points) Describe the effect on the aircraft industry.
3. (20 points) (a) Define the universe. Give three examples.
(b) If the universe were to end, how would you know?
The above example illustrates several things:
• Parts of a question should be put into a parts environment.
• If a question begins with a parts environment, then the first part will appear on the
same line with the question number.
• You can leave blank lines before and after the \part command, and they will be
ignored.
• You can assign points either to the question or to the parts of a question.
2.5 Leaving space for the answers
To leave blank space after a question you use the \vspace command, and you end a page
with the \newpage command. For example, if you wanted to leave 3 inches of space after
the first question and 2 inches of space after each of the parts of the second question, your
questions environment would contain the following:
\question[10]
Why is there air?
\vspace{3in}
\question
What if there were no air?
Page 9

\begin{parts}
\part[5]
| Describe | the | effect | on  | the | balloon | industry. |     |
| -------- | --- | ------ | --- | --- | ------- | --------- | --- |
\vspace{2in}
\part[5]
| Describe | the | effect | on  | the | aircraft | industry. |     |
| -------- | --- | ------ | --- | --- | -------- | --------- | --- |
\vspace{2in}
\end{parts}
\newpage
If you want to equally distribute the space on a page among several questions (or parts, or
| subparts, | or  | subsubparts), |     | you should |     | type |     |
| --------- | --- | ------------- | --- | ---------- | --- | ---- | --- |
\vspace{\stretch{1}}
after each of the questions (or parts, etc.) and end the page with \newpage. If you’d
like one of those questions to receive twice as much space as each of the others, then
follow that one question with \vspace{\stretch{2}} and follow each of the others with
\vspace{\stretch{1}}. (You can use any decimal number for the \stretch value. For
example, \vspace{\stretch{1.5}} will allocate 1.5 times the amount of space allocated by
\vspace{\stretch{1}}.)
In addition to leaving blank space, it’s also possible to leave lined space, dotted lined
space, space printed with a grid, or an empty box. For the full story, see section 7.
| 2.6        | Headers |     | and | footers  |          |             |     |
| ---------- | ------- | --- | --- | -------- | -------- | ----------- | --- |
| To produce | headers |     | and | footers, | you give | the command |     |
\pagestyle{headandfoot}
inthepreamble(i.e., afterthe\documentclasscommandandbeforethe\begin{document}
command), followed by the commands that say what will be in the headers and footers.
Headers and footers each have three parts: One part on the left, one centered part, and one
| part on          | the right, | and | any     | of these | can        | be empty.    |          |
| ---------------- | ---------- | --- | ------- | -------- | ---------- | ------------ | -------- |
| The              | headers    | and | footers | are      | determined | by the       | commands |
| \firstpageheader |            |     |         | for      | the header | on the first | page,    |
| \firstpagefooter |            |     |         | for      | the footer | on the first | page,    |
\firstpageheadrule to put a horizontal rule in the head of the first page,
\firstpagefootrule to put a horizontal rule in the foot of the first page,
| \runningheader |     |     |     | for | the header | after the | first page, |
| -------------- | --- | --- | --- | --- | ---------- | --------- | ----------- |
| \runningfooter |     |     |     | for | the footer | after the | first page  |
\runningheadrule to put a horizontal rule in the head after the first page, and
\runningfootrule to put a horizontal rule in the foot after the first page.
| For | example, | to  | have | the header |     |         |     |
| --- | -------- | --- | ---- | ---------- | --- | ------- | --- |
|     |          |     |      |            |     | Page 10 |     |

| Math 115 |             |     |        |     |       | First | Exam |        | July 4, | 1776 |
| -------- | ----------- | --- | ------ | --- | ----- | ----- | ---- | ------ | ------- | ---- |
| on the   | first page, | the | header |     |       |       |      |        |         |      |
| Math 115 |             |     |        |     | First | Exam, | Page | 2 of 5 | July 4, | 1776 |
on all pages after the first, and no footer on any page, give the commands
\pagestyle{headandfoot}
\runningheadrule
| \firstpageheader{Math |     |        |     | 115}{First |      | Exam}{July |     | 4, 1776}      |     |     |
| --------------------- | --- | ------ | --- | ---------- | ---- | ---------- | --- | ------------- | --- | --- |
| \runningheader{Math   |     |        |     | 115}       |      |            |     |               |     |     |
|                       |     | {First |     | Exam,      | Page | \thepage\  |     | of \numpages} |     |     |
|                       |     | {July  |     | 4, 1776}   |      |            |     |               |     |     |
\firstpagefooter{}{}{}
\runningfooter{}{}{}
| For      | another | example, |     | to have | the | header |      |     |         |      |
| -------- | ------- | -------- | --- | ------- | --- | ------ | ---- | --- | ------- | ---- |
| Math 115 |         |          |     |         |     | First  | Exam |     | July 4, | 1776 |
on the first page, no header on the pages after the first, no footer on the first page, and the
footer
| Math 115     |     |       |            |      |     | First    | Exam |     | Page 2 | of 5 |
| ------------ | --- | ----- | ---------- | ---- | --- | -------- | ---- | --- | ------ | ---- |
| on all pages |     | after | the first, | give | the | commands |      |     |        |      |
\pagestyle{headandfoot}
| \firstpageheader{Math |     |     |     | 115}{First |     | Exam}{July |     | 4, 1776} |     |     |
| --------------------- | --- | --- | --- | ---------- | --- | ---------- | --- | -------- | --- | --- |
\runningheader{}{}{}
\firstpagefooter{}{}{}
\runningfooter{Math 115}{First Exam}{Page \thepage\ of \numpages}
\runningfootrule
Sections 11.10.1 through 11.10.8 contain many other examples of headers and footers,
and the full explanation of the commands for headers and footers (including header and
footer commands other than the ones we’ve just mentioned) is in sections 11.1–11.9.
| 3 The |     | \documentclass |     |     |     | command |     |     |     |     |
| ----- | --- | -------------- | --- | --- | --- | ------- | --- | --- | --- | --- |
To use the exam document class, you should specify exam as the required argument to your
| \documentclass |     | command, |     |     | as in |     |     |     |     |     |
| -------------- | --- | -------- | --- | --- | ----- | --- | --- | --- | --- | --- |
\documentclass{exam}
| or, e.g., | if you | want | to use | 12  | point | type, |     |     |     |     |
| --------- | ------ | ---- | ------ | --- | ----- | ----- | --- | --- | --- | --- |
|           |        |      |        |     |       | Page  | 11  |     |     |     |

\documentclass[12pt]{exam}
There are two possible optional arguments that are specific to the exam document class:
addpoints and solutions. Most documents that use the exam document class should use
the option addpoints (see section 3.1); the option answers is used when you want to print
solutions to the questions (see section 3.2).
3.1 The option addpoints
The \documentclass option addpoints, used as in
\documentclass[addpoints]{exam}
or
\documentclass[12pt,addpoints]{exam}
enables the commands that add up the points (see sections 4.3.9, 4.7, 9.5, and 9.6) and
that produce grading tables and point tables (see sections 9.1 and 9.2). This is an option,
rather than the default, mainly for the sake of maintaining backward compatibility; most
documents that use the exam document class should use this option. The only reason not
to use the addpoints option is that this option creates an error if you include any words
in an argument that assigns points to a question (see section 4.3). If addpoints is not in
effect you can put whatever you want in the argument for the points, but if addpoints is in
effect then the argument that contains the points must contain only digits and the command
\half (see section 4.3.3).
You can also turn addpoints on and off wherever you like in the exam by using the
commands
\addpoints
\noaddpoints
Usingthedocumentclassoptionaddpointsisequivalenttogivingthecommand\addpoints
at the beginning of the exam.
3.2 The option answers
If you will be typing solutions into the exam (see sections 8, 5.5, and 7.7) and you’d like
the solutions to be printed on the next run of LATEX, you should include the document class
option answers, as in
\documentclass[answers]{exam}
or
\documentclass[answers,12pt]{exam}
or
Page 12

\documentclass[12pt,addpoints,answers]{exam}
Usingthedocumentclassoptionanswersisequivalenttogivingthecommand\printanswers
at the beginning of the exam (see section 8). The effect of this is that
• the contents of the environments
solution,
solutionorbox,
solutionorlines,
solutionordottedlines,
solutionorgrid, and
solutionbox
(see section 8) will be printed,
• any choices of a choices, oneparchoices, checkboxes, or oneparcheckboxes en-
vironment (see section 5) that are created using a \CorrectChoice command (see
section 5.5) instead of a \choice command will be printed with emphasis as deter-
mined by the argument of the most recent \CorrectChoiceEmphasis command (which
by default is \bfseries), and
• any \answerline commands (see section 7.6) that include an optional argument con-
taining the answer (see section 7.7) will have the answer printed on the answer line.
4 Questions and points
To create questions, you use a questions environment (see section 4.1); each question is
begunwitha\questioncommand, whichtakesanoptionalargumenttoassignsomenumber
of points to the question (see section 4.3). The questions are numbered automatically. Point
values can include half points (see section 4.3.3).
If you want a question to have several parts, you use a parts environment (see sec-
tion 4.2); each part is begun with a \part command, which takes an optional argument
to assign some number of points to the part (see section 4.3). The parts are numbered
automatically. Similarly, parts can have subparts, and subparts can have subsubparts (see
section 4.2).
The points for a question (or part, or subpart, or subsubpart) appear by default at
the beginning of the question (or part, etc.), but there are commands to have the points
appear instead in either the left margin or in the right margin (see section 4.3.1 and sec-
tion 4.3.2). The formatting of the points can also be customized (see sections 4.3.4, 4.3.5,
4.3.6, and 4.3.7). It’s also possible to have questions (or parts, etc.) that are worth “bonus
points”, which are added up separately from the non-bonus points (see section 4.6).
Page 13

4.1 Questions
To type the questions on the exam you use the questions environment. Each question is
then begun with the command \question, and the questions are numbered automatically.
| For example, | if you type |     |     |
| ------------ | ----------- | --- | --- |
\begin{questions}
\question
| Why is | there air? |     |     |
| ------ | ---------- | --- | --- |
\question
How much wood would a woodchuck chuck if a woodchuck could chuck
wood?
| \question | Compute $\displaystyle\int_0^1 |     | x^2 \, dx$. |
| --------- | ------------------------------ | --- | ----------- |
\end{questions}
| then you’ll | get           |     |     |
| ----------- | ------------- | --- | --- |
| 1. Why      | is there air? |     |     |
2. How much wood would a woodchuck chuck if a woodchuck could chuck wood?
(cid:90) 1
| 3. Compute | x2dx. |     |     |
| ---------- | ----- | --- | --- |
0
As the above example illustrates, you can leave blank lines between the \question com-
mand and the actual beginning of the question, or before the first \question command in
| the environment, | and they will | be ignored.        |                   |
| ---------------- | ------------- | ------------------ | ----------------- |
| 4.2 Questions    | with          | parts and subparts | (and subsubparts) |
If you want a question to have several parts, then you use the parts environment. For
| example, | if you type |     |     |
| -------- | ----------- | --- | --- |
\begin{questions}
\question
| Why is | there air? |     |     |
| ------ | ---------- | --- | --- |
\question
| What if | there were no air? |     |     |
| ------- | ------------------ | --- | --- |
\begin{parts}
\part
Page 14

Describe the effect on the balloon industry.
\part
Describe the effect on the aircraft industry.
\end{parts}
\question
\begin{parts}
\part
Define the universe. Give three examples.
\part
If the universe were to end, how would you know?
\end{parts}
\end{questions}
then you’ll get
1. Why is there air?
2. What if there were no air?
(a) Describe the effect on the balloon industry.
(b) Describe the effect on the aircraft industry.
3. (a) Define the universe. Give three examples.
(b) If the universe were to end, how would you know?
The above example illustrates several things:
• Parts of a question should be put into a parts environment.
• If a question begins with a parts environment, then the first part will appear on the
same line with the question number.
• You can leave blank lines before and after the \part command, and they will be
ignored.
There is also a subparts environment, and even a subsubparts environment, and they
work just as you would expect. For example, if you type
Page 15

\begin{questions}
\question
\begin{parts}
\part
| What do | you | do with | a drunken | sailor? |
| ------- | --- | ------- | --------- | ------- |
\part
| Is your | answer | different | if  | it is before noon? |
| ------- | ------ | --------- | --- | ------------------ |
\end{parts}
\question
| This is | the | second | question. |     |
| ------- | --- | ------ | --------- | --- |
\begin{parts}
\part
| This is | a part. |     |     |     |
| ------- | ------- | --- | --- | --- |
\part
| This is | also | a part. |     |     |
| ------- | ---- | ------- | --- | --- |
\begin{subparts}
\subpart
| This is | a subpart. |     |     |     |
| ------- | ---------- | --- | --- | --- |
\subpart
| This is | a periscope. |     |     |     |
| ------- | ------------ | --- | --- | --- |
\subpart
| This is | a pair | of  | diving planes. |     |
| ------- | ------ | --- | -------------- | --- |
\subpart
\begin{subsubparts}
\subsubpart
| This is | a subsubpart. |     |     |     |
| ------- | ------------- | --- | --- | --- |
\subsubpart
| The lower | surface |     | of a diving | plane? |
| --------- | ------- | --- | ----------- | ------ |
\subsubpart
| The ocean | floor, | perhaps? |     |     |
| --------- | ------ | -------- | --- | --- |
\end{subsubparts}
\end{subparts}
Page 16

\part
It’s sad to be apart.
\end{parts}
\question
\begin{parts}
\part
\begin{subparts}
\subpart
This is a subpart.
\subpart
This is another subpart.
\end{subparts}
\part
This is another part.
\end{parts}
\end{questions}
then you’ll get
1. (a) What do you do with a drunken sailor?
(b) Is your answer different if it is before noon?
2. This is the second question.
(a) This is a part.
(b) This is also a part.
i. This is a subpart.
ii. This is a periscope.
iii. This is a pair of diving planes.
iv. ?) This is a subsubpart.
?) The lower surface of a diving plane?
?) The ocean floor, perhaps?
(c) It’s sad to be apart.
3. (a) i. This is a subpart.
ii. This is another subpart.
Page 17

(b) This is another part.
The numbers and letters used to number questions, parts, subparts, and subsubparts can
be customized; see section 4.9.
4.3 Point values for the questions
Each of the commands \question, \part, \subpart, and \subsubpart takes an optional
argument, which is the number of points for that question, part, subpart, or subsubpart.
The default setup is that
• the point value is printed at the beginning of the question (or part, or subpart, or
subsubpart) (this can be changed to printing in either the left or right margins on
the first line of the question or in the right margin at the end of the question; see
section 4.3.1 and section 4.3.2), and
• thepointvalueisenclosedinparentheses(thiscanbechangedtoeithersquarebrackets
or a box; see section 4.3.4).
Both of these things can be further customized; see section 4.4 and section 4.3.7.
4.3.1 Where the points will be printed
The default is that the point value will be inserted at the beginning of the question (or part,
or subpart, or subsubpart) in parentheses, but
• thecommand\pointsinmargin(or,equivalently,thecommand\pointsinleftmargin)
will cause the point values to be set in the left margin,
• the command \pointsinrightmargin will cause the point values to be set in the right
margin,
• the command \pointstwosided will cause the point values to be set
– in the right margin on odd numbered pages and
– in the left margin on even numbered pages,
• the command \pointstwosidedreversed will cause the point values to be set
– in the left margin on odd numbered pages and
– in the right margin on even numbered pages, and
• thecommands\nopointsinmarginand\nopointsinrightmarginareequivalent, and
either of them will revert to the default situation.
All of these print the point values on the first line of the question (or part, or subpart, or
subsubpart). There is also a way to print the point values on the last line of the question
(or part, etc.); for this, see section 4.3.2.
Page 18

|     | For | example, |     | if you | type |     |     |     |     |
| --- | --- | -------- | --- | ------ | ---- | --- | --- | --- | --- |
\begin{questions}
\question[20]
|     | Why is | there | air? |     |     |     |     |     |     |
| --- | ------ | ----- | ---- | --- | --- | --- | --- | --- | --- |
\question
|     | What | if there | were |     | no air? |     |     |     |     |
| --- | ---- | -------- | ---- | --- | ------- | --- | --- | --- | --- |
\begin{parts}
\part[10]
|     | Describe | the | effect |     | on the | balloon | industry. |     |     |
| --- | -------- | --- | ------ | --- | ------ | ------- | --------- | --- | --- |
\part[10]
|     | Describe | the | effect |     | on the | aircraft | industry. |     |     |
| --- | -------- | --- | ------ | --- | ------ | -------- | --------- | --- | --- |
\end{parts}
\end{questions}
|     | then,   | with the | default |          | setup, you’ll | get    |        |                    |     |
| --- | ------- | -------- | ------- | -------- | ------------- | ------ | ------ | ------------------ | --- |
|     | 1. (20  | points)  | Why     | is       | there air?    |        |        |                    |     |
|     | 2. What | if       | there   | were     | no air?       |        |        |                    |     |
|     | (a)     | (10      | points) | Describe | the           | effect | on the | balloon industry.  |     |
|     | (b)     | (10      | points) | Describe | the           | effect | on the | aircraft industry. |     |
(To change the word “points”, see the commands described in section 4.3.5.)
If you give the command \pointsinmargin (or, equivalently, \pointsinleftmargin),
|      | then    | the above | input | will | produce   | instead      |           |     |     |
| ---- | ------- | --------- | ----- | ---- | --------- | ------------ | --------- | --- | --- |
| (20) | 1. Why  | is        | there | air? |           |              |           |     |     |
|      | 2. What | if        | there | were | no air?   |              |           |     |     |
| (10) | (a)     | Describe  |       | the  | effect on | the balloon  | industry. |     |     |
| (10) | (b)     | Describe  |       | the  | effect on | the aircraft | industry. |     |     |
(To have a word (e.g., “points”, or “%”) inside the parentheses with the point values, see
|     | the \marginpointname |     |     |     | command | in section |     | 4.3.5.) |     |
| --- | -------------------- | --- | --- | --- | ------- | ---------- | --- | ------- | --- |
If you give the command \pointsinrightmargin, then the above input will produce
instead
|     | 1. Why | is  | there | air? |     |     |      |     | (20) |
| --- | ------ | --- | ----- | ---- | --- | --- | ---- | --- | ---- |
|     |        |     |       |      |     |     | Page | 19  |      |

| 2. What | if there | were | no air? |                 |           |          |      |
| ------- | -------- | ---- | ------- | --------------- | --------- | -------- | ---- |
| (a)     | Describe | the  | effect  | on the balloon  | industry. |          | (10) |
| (b)     | Describe | the  | effect  | on the aircraft | industry. |          | (10) |
| 4.3.2   | Printing | the  | points  | at the end      | of the    | question |      |
Instead of having the point value of a question (or part, or subpart, or subsubpart) printed
on the first line of a question, you can have it printed in the right margin opposite the last
line, or even opposite a blank line following the paragraph. This is done with the
|     |     |     | \pointsdroppedatright |     |     | and \droppoints |     |
| --- | --- | --- | --------------------- | --- | --- | --------------- | --- |
commands.
| If  | you give | the command |     |     |     |     |     |
| --- | -------- | ----------- | --- | --- | --- | --- | --- |
\pointsdroppedatright
then point values are not printed until you give the command \droppoints (and they’re not
printed at all if you don’t give the command \droppoints). The only exception to this rule
is that if you’ve given a \qformat command (see section 4.4), then question number lines
are printed as specified by the argument to the \qformat command even if you have given
| the command |     | \pointsdroppedatright |     |     |     |     |     |
| ----------- | --- | --------------------- | --- | --- | --- | --- | --- |
The command \droppoints should be given only at the end of a paragraph or between
paragraphs; if you give it within a paragraph, it causes the paragraph to end. \droppoints
prints the point value in the right margin, formatted as it is when you give the command
\pointsinrightmargin,exceptthatthepointsappearoppositethelastlineoftheparagraph
(or, ifthecommand\droppointsisgivenbetweenparagraphs, thenadditionalverticalspace
is left between the paragraphs and the points are printed opposite the blank space). The
formatting can be changed by giving the commands \bracketedpoints, \boxedpoints, or
\marginpointname (see section 4.3.5) just as if \pointsinrightmargin were in effect. The
command \droppoints actually works this way even if one of the commands
|     | \nopointsinmargin, |     |     | \pointsinmargin, |     | or \pointsinrightmargin |     |
| --- | ------------------ | --- | --- | ---------------- | --- | ----------------------- | --- |
is in effect, but if you use it that way the points will appear twice on the page, which is
| probably | not what | you | want. |     |     |     |     |
| -------- | -------- | --- | ----- | --- | --- | --- | --- |
For example, if you give the command \pointsdroppedatright and then type
\begin{questions}
\question[10]
Describe the implications of the Michelson-Morley ink drop experiment
for the use of punctuation marks such as colons and semicolons that
| require | multiple |     | drops | of ink. |     |     |     |
| ------- | -------- | --- | ----- | ------- | --- | --- | --- |
\droppoints
\question[10]
Page 20

Prove that the second dual of a finite dimensional real vector space
is naturally isomorphic to the given vector space, except when the
| weapon chosen | is a single | shot pistol.\droppoints |
| ------------- | ----------- | ----------------------- |
\end{questions}
| then you’ll get |     |     |
| --------------- | --- | --- |
1. Describe the implications of the Michelson-Morley ink drop experiment for the use of
punctuation marks such as colons and semicolons that require multiple drops of ink. (10)
2. Prove that the second dual of a finite dimensional real vector space is naturally isomor-
phic to the given vector space, except when the weapon chosen is a single shot pistol. (10)
| and if you type |     |     |
| --------------- | --- | --- |
\begin{questions}
\question[10]
Describe the implications of the Michelson-Morley ink drop experiment
for the use of punctuation marks such as colons and semicolons that
| require multiple | drops | of ink. |
| ---------------- | ----- | ------- |
\droppoints
\question[10]
Prove that the second dual of a finite dimensional real vector space
is naturally isomorphic to the given vector space, except when the
| weapon chosen | is a single | shot pistol. |
| ------------- | ----------- | ------------ |
\droppoints
\end{questions}
| then you’ll get |     |     |
| --------------- | --- | --- |
1. Describe the implications of the Michelson-Morley ink drop experiment for the use of
punctuation marks such as colons and semicolons that require multiple drops of ink.
(10)
2. Prove that the second dual of a finite dimensional real vector space is naturally isomor-
phic to the given vector space, except when the weapon chosen is a single shot pistol.
(10)
Page 21

| 4.3.3 Half | points |     |     |     |     |     |     |     |     |
| ---------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
The point values of questions, parts, subparts, and subsubparts can include half points. To
| specify half | points, | you | either | type |     |     |     |     |     |
| ------------ | ------- | --- | ------ | ---- | --- | --- | --- | --- | --- |
\half
immediately following the integer part of the point value or just type \half as the entire
point value. That is, the valid point values and their (default) printed appearances are:
|     | Typed:   |     | 0   | \half | 1   | 1\half | 2   | 2\half | ··· |
| --- | -------- | --- | --- | ----- | --- | ------ | --- | ------ | --- |
|     | Printed: |     | 0   | 1/    | 1   | 11/    | 2   | 21/    | ··· |
|     |          |     |     | 2     |     | 2      |     | 2      |     |
1.
If you prefer, you can cause the fraction 1/ to be printed as To do this, you give the
|     |     |     |     |     |     | 2   |     | 2   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
command
\usehorizontalhalf
| after which | the printed |     | appearance | of    | point | values will | be  |        |     |
| ----------- | ----------- | --- | ---------- | ----- | ----- | ----------- | --- | ------ | --- |
|             | Typed:      |     | 0          | \half | 1     | 1\half      | 2   | 2\half | ··· |
|             | Printed:    |     | 0          | 1     | 1     | 11          | 2   | 21     | ··· |
|             |             |     |            | 2     |       | 2           |     | 2      |     |
Ifyouwanttoreturntousingthedefaultappearance,youcandothatbygivingthecommand
\useslantedhalf
4.3.4 Surrounding the points: Parentheses, brackets, or a box
If you prefer having the points enclosed in brackets instead of in parentheses, give the com-
mand
\bracketedpoints
For example, if you give the command \bracketedpoints, then the questions typed above
will produce
| 1. [20 points] | Why         | is       | there air? |        |        |          |           |     |     |
| -------------- | ----------- | -------- | ---------- | ------ | ------ | -------- | --------- | --- | --- |
| 2. What        | if there    | were     | no air?    |        |        |          |           |     |     |
| (a)            | [10 points] | Describe | the        | effect | on the | balloon  | industry. |     |     |
| (b)            | [10 points] | Describe | the        | effect | on the | aircraft | industry. |     |     |
If you prefer having the points enclosed in a box instead of in parentheses, give the
command
\boxedpoints
Page 22

For example, if you give the command \boxedpoints, then the questions typed above will
produce
|     | 1. 20   | points | Why    | is there | air? |        |                           |     |
| --- | ------- | ------ | ------ | -------- | ---- | ------ | ------------------------- | --- |
|     | 2. What | if     | there  | were no  | air? |        |                           |     |
|     | (a)     | 10     | points | Describe | the  | effect | on the balloon industry.  |     |
|     | (b)     | 10     | points | Describe | the  | effect | on the aircraft industry. |     |
If you give the commands \boxedpoints and \pointsinmargin, then the above questions
|     | will produce |          |       |            |      |              |           |     |
| --- | ------------ | -------- | ----- | ---------- | ---- | ------------ | --------- | --- |
| 20  | 1. Why       | is       | there | air?       |      |              |           |     |
|     | 2. What      | if       | there | were no    | air? |              |           |     |
| 10  | (a)          | Describe |       | the effect | on   | the balloon  | industry. |     |
| 10  | (b)          | Describe |       | the effect | on   | the aircraft | industry. |     |
If you give the commands \bracketedpoints and \pointsinrightmargin, then the above
|     | questions | will     | produce |            |      |              |           |      |
| --- | --------- | -------- | ------- | ---------- | ---- | ------------ | --------- | ---- |
|     | 1. Why    | is       | there   | air?       |      |              |           | [20] |
|     | 2. What   | if       | there   | were no    | air? |              |           |      |
|     | (a)       | Describe |         | the effect | on   | the balloon  | industry. | [10] |
|     | (b)       | Describe |         | the effect | on   | the aircraft | industry. | [10] |
Other combinations of these commands will produce similar effects.
If you want to switch back and forth between formats during the exam, you can do so
|     | by giving | one | of the | commands |     |     |     |     |
| --- | --------- | --- | ------ | -------- | --- | --- | --- | --- |
\boxedpoints
\bracketedpoints
\noboxedpoints
\nobracketedpoints
whenever you want to switch. (The commands \nobracketedpoints and \noboxedpoints
are equivalent; they both return to the default of putting parentheses around the points.)
Ifyouwantsometext(e.g., “points”, or“%”)automaticallyinsertedalongwiththepoint
values when using either \pointsinmargin, \pointsinrightmargin, \pointstwosided, or
\pointstwosidedreversed, see the command \marginpointname in section 4.3.5.
Page 23

| 4.3.5 | Using | a substitute |     | for the | word | “points” |     |
| ----- | ----- | ------------ | --- | ------- | ---- | -------- | --- |
With the default setup, the number of points is inserted before the text of the question
followed by a single space and the word “point” if the number of points is either 1/ or
2
1 and by the word “points” otherwise. That is, the default is \nopointsinmargin and
| \noboxedpoints |     | (see | sections | 4.3.1 | and 4.3.4), |     | and if you type |
| -------------- | --- | ---- | -------- | ----- | ----------- | --- | --------------- |
\begin{questions}
\question[1]
|     | This is | a short | question. |     |     |     |     |
| --- | ------- | ------- | --------- | --- | --- | --- | --- |
\question[5]
|     | This is | a longer | question, | requiring |     |     | more thought. |
| --- | ------- | -------- | --------- | --------- | --- | --- | ------------- |
\end{questions}
| then | you’ll     | get          |          |           |           |     |               |
| ---- | ---------- | ------------ | -------- | --------- | --------- | --- | ------------- |
| 1.   | (1 point)  | This is      | a short  | question. |           |     |               |
| 2.   | (5 points) | This is      | a longer | question, | requiring |     | more thought. |
| The  | way this   | is achieved  | is:      |           |           |     |               |
|      | • There    | is a command |          |           |           |     |               |
\points
whose default definition expands to the word ‘point’ if the number of points is either
1/ or 1 and to ‘points’ otherwise. (This behavior can be modified by the command
2
|     | \pointpoints; |     | see below.) |     |     |     |     |
| --- | ------------- | --- | ----------- | --- | --- | --- | --- |
•
|     | There | is a command |     |     |     |     |     |
| --- | ----- | ------------ | --- | --- | --- | --- | --- |
\pointname{Text}
that causes ‘Text’ to be inserted following the number of points of a question, part,
subpart, or subsubpart. The default setup is the result of the command
|     |       |                   |       |            | \pointname{ |     | \points}  |
| --- | ----- | ----------------- | ----- | ---------- | ----------- | --- | --------- |
|     | (Note | the single        | space | before the | command     |     | \points.) |
|     | There | is also a command |       |            |             |     |           |
\pointpoints{SingularText}{PluralText}
that changes the behavior of the \points command so that it expands to ‘SingularText’ if
the number of points is 1/ or 1 and to ‘PluralText’ otherwise. (The default is the result of
2
the command \pointpoints{point}{points}.) Thus, if you give the command
|     |     |     |     |     |     | Page | 24  |
| --- | --- | --- | --- | --- | --- | ---- | --- |

\pointpoints{Punkt}{Punkte}
|     | then typing |         | the questions | above    |           | would     | result | in        |               |     |
| --- | ----------- | ------- | ------------- | -------- | --------- | --------- | ------ | --------- | ------------- | --- |
|     | 1. (1       | Punkt)  | This is       | a short  | question. |           |        |           |               |     |
|     | 2. (5       | Punkte) | This is       | a longer |           | question, |        | requiring | more thought. |     |
|     | There       | is also | a command     |          |           |           |        |           |               |     |
\marksnotpoints
|     | that is | equivalent | to the | two | commands |     |     |     |     |     |
| --- | ------- | ---------- | ------ | --- | -------- | --- | --- | --- | --- | --- |
\pointpoints{mark}{marks}
|     |     |     | \bonuspointpoints{mark |     |     |     |     | (bonus)}{marks |     | (bonus)} |
| --- | --- | --- | ---------------------- | --- | --- | --- | --- | -------------- | --- | -------- |
(the command \bonuspointpoints is described in section 4.6). That command would cause
|     | the above | questions | to       | be printed |           | as       |           |     |               |     |
| --- | --------- | --------- | -------- | ---------- | --------- | -------- | --------- | --- | ------------- | --- |
|     | 1. (1     | mark)     | This is  | a short    | question. |          |           |     |               |     |
|     | 2. (5     | marks)    | This is  | a longer   | question, |          | requiring |     | more thought. |     |
|     | For       | another   | example, | if         | you       | give the | command   |     |               |     |
\pointname{\%}
|     | then the | above            | questions   | would     |     | be printed |     | as   |          |     |
| --- | -------- | ---------------- | ----------- | --------- | --- | ---------- | --- | ---- | -------- | --- |
|     | 1. (1%)  | This             | is a short  | question. |     |            |     |      |          |     |
|     | 2. (5%)  | This             | is a longer | question, |     | requiring  |     | more | thought. |     |
|     | Using    | \marginpointname |             |           |     |            |     |      |          |     |
Similarly, the command \marginpointname can be used to affect the text set with the num-
ber of points when \pointsinmargin or \pointsinrightmargin is in effect. For example,
|     | if you give | the | commands |     |     |     |     |     |     |     |
| --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
\pointsinmargin
\marginpointname{\%}
|     | and then | type |     |     |     |     |     |     |     |     |
| --- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
\question[25]
|       | Where,      | oh  | where, has | my  | little    |     | dog   | gone? |     |     |
| ----- | ----------- | --- | ---------- | --- | --------- | --- | ----- | ----- | --- | --- |
|       | then you’ll | get |            |     |           |     |       |       |     |     |
| (25%) | 1. Where,   |     | oh where,  | has | my little | dog | gone? |       |     |     |
|       |             |     |            |     |           |     | Page  |       | 25  |     |

unless, e.g., you’ve also given the command \boxedpoints (see section 4.3.4), in which case
you’ll get
| 25% | 1. Where, | oh where,         | has my little | dog gone? |     |
| --- | --------- | ----------------- | ------------- | --------- | --- |
|     | If you    | give the commands |               |           |     |
\marksnotpoints
|            |           |             | \marginpointname{ |               | \points} |
| ---------- | --------- | ----------- | ----------------- | ------------- | -------- |
|            | then the  | above will  | print             |               |          |
| (25 marks) | 1. Where, | oh where,   | has my little     | dog gone?     |          |
|            | Using     | the default | is equivalent     | to giving the | command  |
\marginpointname{}
|     | 4.3.6 | Using |     | and enlarging | the margins |
| --- | ----- | ----- | --- | ------------- | ----------- |
\marginpointname
The default margins are not very large, and so if you use \marginpointname (see sec-
tion 4.3.5) to place any words along with the point values in the margin, you may run out
of room. The solution to this problem is to enlarge the margins by using the \extrawidth
command with a negative argument to decrease the width of the text area, and thus increase
|     | the width | of the margins. | For example, | the commands |     |
| --- | --------- | --------------- | ------------ | ------------ | --- |
\extrawidth{-1in}
|     |     |     | \marginpointname{ |     | \points} |
| --- | --- | --- | ----------------- | --- | -------- |
will increase each of the left and right margins by one half inch, which will easily leave room
for the word “points”. (See section 10 for a discussion of the \extrawidth command.)
|     | 4.3.7 | Completely | customizing | the points |     |
| --- | ----- | ---------- | ----------- | ---------- | --- |
If the customizations described in section 4.3.4 and section 4.3.5 (using \bracketedpoints,
\boxedpoints, \pointpoints, \pointname, and \marginpointname) aren’t sufficient, and
you don’t want to use the \qformat command to create a customized question number line
(see section 4.4), you can completely customize the way the points are printed by using the
commands
\pointformat
\bonuspointformat
The \pointformat command controls the printing of “regular” points (i.e., non-bonus
points) and the \bonuspointformat command controls the printing of bonus points (see
section 4.6).
Each of the commands \pointformat and \bonuspointformat takes one argument, and
that argument is what actually appears on the page whether the points are being printed at
thebeginningofthequestion(thedefault), intheleftmargin(becauseof\pointsinmargin),
in the right margin (because of \pointsinrightmargin), or dropped in the right mar-
gin at the end of the question (because of \pointsdroppedatright). The arguments to
\pointformat and \bonuspointformat should contain either the command
|     |     |     |     | Page | 26  |
| --- | --- | --- | --- | ---- | --- |

\thepoints
(which for non-bonus points prints the number of points followed by the argument to the
last \pointname command and for bonus points prints the number of bonus points followed
by the argument to the last \bonuspointname command; see section 4.3.5) or the command
\themarginpoints
(which for non-bonus points prints the number of points followed by the argument to the
last \marginpointname command and for bonus points prints the number of bonus points
followed by the argument to the last \marginbonuspointname command; see section 4.3.5).
If the argument doesn’t contain either \thepoints or \themarginpoints, then the number
|     | of points | will not appear. |     |     |     |
| --- | --------- | ---------------- | --- | --- | --- |
For example, the command \bracketedpoints is equivalent to either
\pointformat{[\thepoints]}
\bonuspointformat{[\thepoints]}
if the points are being printed at the beginning of the question, or
\pointformat{[\themarginpoints]}
\bonuspointformat{[\themarginpoints]}
|     | if the points | are being | printed | in one of the | margins. |
| --- | ------------- | --------- | ------- | ------------- | -------- |
For another example, the command \boxedpoints is equivalent to either
\pointformat{\fbox{\thepoints}}
\bonuspointformat{\fbox{\thepoints}}
if the points are being printed at the beginning of the question, or
\pointformat{\fbox{\themarginpoints}}
\bonuspointformat{\fbox{\themarginpoints}}
|     | if the points | are being | printed | in one of the | margins. |
| --- | ------------- | --------- | ------- | ------------- | -------- |
|     | For another   | example,  | the     | commands      |          |
\begin{questions}
\pointsinmargin
\marginpointname{\%}
|     | \pointformat{\slshape |      |     | (\themarginpoints)} |     |
| --- | --------------------- | ---- | --- | ------------------- | --- |
|     | \question[3]          | What | is  | the point?          |     |
\end{questions}
|      | will produce |               |     |          |     |
| ---- | ------------ | ------------- | --- | -------- | --- |
| (3%) | 1. What      | is the point? |     |          |     |
|      | For another  | example,      | the | commands |     |
Page 27

\begin{questions}
\pointsinrightmargin
\marginpointname{\%}
\pointformat{\fbox{\bfseries\boldmath\themarginpoints}}
| \question[3\half] |     | What | is the | point? |     |     |
| ----------------- | --- | ---- | ------ | ------ | --- | --- |
\end{questions}
will produce
| 1. What | is the | point? |     |     |     | 31/% |
| ------- | ------ | ------ | --- | --- | --- | ---- |
2
(Note: The commands \bfseries and \boldmath are both needed here because the 1/
2
printed when you use half points is printed in math mode while the rest of the points are
| printed | in text mode.)   |     |          |     |     |     |
| ------- | ---------------- | --- | -------- | --- | --- | --- |
| For     | another example, | the | commands |     |     |     |
\begin{questions}
\pointname{}
\pointformat{\bfseries\boldmath(Points for this problem: \thepoints)}
| \question[3\half] |     | What | is the | point? |     |     |
| ----------------- | --- | ---- | ------ | ------ | --- | --- |
\end{questions}
will produce
| 1. (Points | for | this problem: | 31/) | What | is the point? |     |
| ---------- | --- | ------------- | ---- | ---- | ------------- | --- |
2
| 4.3.8 | Questions | that | begin with | a parts | environment |     |
| ----- | --------- | ---- | ---------- | ------- | ----------- | --- |
If a question begins with a parts environment, then the question number and the number
of the first part in the parts environment will be printed on the same line (see section 4.2).
Thus, if points are assigned to both the question and to the first part, both of those point
values will be printed on the same line. (Note: This was not true in versions of the exam
document class earlier than 2.3. In those versions, only the later of the two point values
would actually be printed.) If \pointsinmargin or \pointsinrightmargin are in effect
(see section 4.3.1), then the two point values will be printed on top of each other, which
is probably not what you want. The same problem arises if a part begins with a subparts
environment or if a subpart begins with a subsubparts environment.
If you want to assign points to both a question and to each part of a parts environment,
and if the first part will begin on the same line as the question, the solution is to either use
the default location (i.e., \nopointsinmargin) or to put some of the points in the margin
| and others | not. | For example, | if you | type |     |     |
| ---------- | ---- | ------------ | ------ | ---- | --- | --- |
\begin{questions}
\pointsinmargin
\noaddpoints
\question[10]
|     |     |     |     | Page | 28  |     |
| --- | --- | --- | --- | ---- | --- | --- |

\begin{parts}
\nopointsinmargin
\addpoints
\part[5] Who put the ‘‘bop’’ in the ‘‘bop, sh-bop, sh-bop’’?
\part[5] Who put the ‘‘ram’’ in the ‘‘rama, rama ding-dong’’?
\end{parts}
\end{questions}
then you’ll get
(10%) 1. (a) (5 points) Who put the “bop” in the “bop, sh-bop, sh-bop”?
(b) (5 points) Who put the “ram” in the “rama, rama ding-dong”?
4.3.9 Adding up the points for a question
Ifyouusethedocumentclassoptionaddpoints(asin\documentclass[addpoints]{exam})
or give the command \addpoints (see section 3.1), then you can use the command
\droptotalpoints
to put into the right margin the total number of points for the current question (including
the points for all parts, subparts, and subsubparts). (Section 4.4.1 describes a different
way to print the total number of points for a question.) The command \droptotalpoints
should be used only at the end of a paragraph or between paragraphs; if you use it within
a paragraph, it causes the paragraph to end. \droptotalpoints prints the total points for
the current question in the right margin, formatted by default as:
Total for Question 2: 25
(Note: The number of points is followed by the argument to the most recently executed
\marginpointname command (see section 4.3.5), which by default is empty.)
If the current question is worth any bonus points (see section 4.6), then those bonus
points will not be counted by the \droptotalpoints command, but they will be counted
by the
\droptotalbonuspoints
command, which puts into the right margin the total number of bonus points for the current
question, formatted by default as:
Total for Question 2: 10 (bonus)
(Note: Thenumberofbonuspointsisfollowedbytheargumenttothemostrecentlyexecuted
\marginbonuspointname command (see section 4.6), which by default is “ (bonus)”.)
You can change the format used by the \droptotalpoints command with the
\totalformat
Page 29

command. It takes one argument, and that argument becomes the command to print the
total points, right justified a distance of \rightpointsmargin from the right edge of the
| paper. | The argument |     | can          | contain | the command |       |              |                |
| ------ | ------------ | --- | ------------ | ------- | ----------- | ----- | ------------ | -------------- |
|        |              |     | \totalpoints |         | to          | print | the number   | of points, and |
|        |              |     | \thequestion |         | to          | print | the question | number.        |
(\totalpoints expands to \pointsofquestion{\arabic{question}}; see section 9.5 for a
discussion of the \pointsofquestion command.) For example, if you give the command
|          |       | \totalformat{Question |     |        |         | \thequestion: |               | \totalpoints} |
| -------- | ----- | --------------------- | --- | ------ | ------- | ------------- | ------------- | ------------- |
| then the | total | number                | of  | points | will be | printed       | in the format |               |
Question 2: 25
| and if you | give  | the    | command                   |        |         |         |                |     |
| ---------- | ----- | ------ | ------------------------- | ------ | ------- | ------- | -------------- | --- |
|            |       |        | \totalformat{\fbox{Total: |        |         |         | \totalpoints}} |     |
| then the   | total | number | of                        | points | will be | printed | as             |     |
Total: 25
| Thus, | if you’ve |     | given | the commands |     |     |     |     |
| ----- | --------- | --- | ----- | ------------ | --- | --- | --- | --- |
\addpoints
\bracketedpoints
\pointsdroppedatright
| and you | type |     |     |     |     |     |     |     |
| ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
\question
\begin{parts}
\part[10]
In no more than one paragraph, explain why the earth is round.
\droppoints
\part[10]
| What changes |       | to   | the van | Allen   | radiation    |     | belt are | needed to |
| ------------ | ----- | ---- | ------- | ------- | ------------ | --- | -------- | --------- |
| make the     | earth | into | a       | regular | icosahedron? |     |          |           |
\droppoints
\end{parts}
\droptotalpoints
| then you’ll | get |     |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
1. (a) In no more than one paragraph, explain why the earth is round. [10%]
(b) What changes to the van Allen radiation belt are needed to make the earth into a
regular icosahedron? [10%]
Total for Question 1: 20
|     |     |     |     |     |     | Page | 30  |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |

| If you’ve also | given | the command |     |     |     |     |
| -------------- | ----- | ----------- | --- | --- | --- | --- |
\totalformat{Total for Question \thequestion: [\totalpoints]}
| then you’ll | get |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
1. (a) In no more than one paragraph, explain why the earth is round. [10%]
(b) What changes to the van Allen radiation belt are needed to make the earth into a
regular icosahedron? [10%]
Total for Question 1: [20]
To change the format used by the \droptotalbonuspoints command, you use the com-
mand
\bonustotalformat
which is analogous to the \totalformat command. The argument to \bonustotalformat
| can contain | the command       |     |          |              |                  |     |
| ----------- | ----------------- | --- | -------- | ------------ | ---------------- | --- |
|             | \totalbonuspoints |     | to print | the number   | of bonus points, | and |
|             | \thequestion      |     | to print | the question | number.          |     |
(\totalbonuspoints expands to \bonuspointsofquestion{\arabic{question}}; see sec-
tion 9.7 for a discussion of the \bonuspointsofquestion command.)
4.3.10 Margin sizes when using \pointsinmargin and \pointsinrightmargin
•
If you give the command \pointsinmargin, then the points are printed right justified
in the left margin, with the right edge a distance of \marginpointssep from the left
edge of the text area. The default value of \marginpointssep is the result of the
command
\setlength{\marginpointssep}{5pt}
| and | you can change | it by | giving a new | \setlength | command. |     |
| --- | -------------- | ----- | ------------ | ---------- | -------- | --- |
•
If you give the command \pointsinrightmargin, then the points are printed right
justified in the right margin, with the right edge a distance of \rightpointsmargin
from the right edge of the paper. The default value of \rightpointsmargin is the
| result | of the command |     |     |     |     |     |
| ------ | -------------- | --- | --- | --- | --- | --- |
\setlength{\rightpointsmargin}{1cm}
| and | you can change | it by | giving a new | \setlength | command. |     |
| --- | -------------- | ----- | ------------ | ---------- | -------- | --- |
You can change the width of the text area (and, thus, change the width of the margins)
| with the \extrawidth |     | command | (see section | 4.3.6). |     |     |
| -------------------- | --- | ------- | ------------ | ------- | --- | --- |
Page 31

| 4.4 | Custom |     | question |     | number |     | lines: | The |     | command |
| --- | ------ | --- | -------- | --- | ------ | --- | ------ | --- | --- | ------- |
\qformat
The default setup is for the question number to appear in the left margin and for the text of
the question to begin on that line. It’s possible to change this so that the text of the question
starts on the line following the question number, and the format of the line containing the
question number is determined by the user. This is done using the \qformat command.
There is also a \noqformat command, which reverts to the default setup.
| To  | use | the \qformat |     | command, |                 | you | give | the command    |     |     |
| --- | --- | ------------ | --- | -------- | --------------- | --- | ---- | -------------- | --- | --- |
|     |     |              |     |          | \qformat{Format |     |      | specification} |     |     |
where Format specification must contain some stretchability (e.g., at least one \hfill
or \dotfill or \hrulefill or ...) and can contain the commands
| •   | \thequestion,     |     |     | which | expands | to      | the question | number,       |     |     |
| --- | ----------------- | --- | --- | ----- | ------- | ------- | ------------ | ------------- | --- | --- |
| •   | \thequestiontitle |     |     | (see  | section | 4.5.2), |              | which expands | to  |     |
– the title of the question, if this question was defined using a \titledquestion
command (see section 4.5.1) instead of a \question command, or
– the number of the question, if this question was defined using a \question com-
mand,
| •   | \thepoints, |     | which | expands |     | to  |     |     |     |     |
| --- | ----------- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- |
– the number of points followed by the argument to the last \pointname command,
|     |     | if there | were | points    | specified |           | for the | question, | or       |     |
| --- | --- | -------- | ---- | --------- | --------- | --------- | ------- | --------- | -------- | --- |
|     | –   | nothing, | if   | no points | were      | specified |         | for the   | question |     |
(see section 4.3.5 for a discussion of the \pointname command), and
•
\totalpoints, which expands to the total number of points specified for the ques-
tion and all of its parts, subparts, and subsubparts (see section 4.3.9). The com-
mand \totalpoints expands to \pointsofquestion{\arabic{question}} (see sec-
|                   | tion | 9.5). |     |              |          |          |     |             |     |     |
| ----------------- | ---- | ----- | --- | ------------ | -------- | -------- | --- | ----------- | --- | --- |
| For example,      |      | if    | you | give the     | commands |          |     |             |     |     |
| \qformat{Question |      |       |     | \thequestion |          | \dotfill |     | \thepoints} |     |     |
\begin{questions}
\question[10]
What did Billy Joe MacAllister throw off the Tallahatchie Bridge?
\end{questions}
| then | you’ll | get |     |     |     |     |     |     |     |     |
| ---- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Question 1.......................................................................10 points
What did Billy Joe MacAllister throw off the Tallahatchie Bridge?
|     |     |     |     |     |     |     | Page | 32  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |

| If you instead | use | the | command |     |     |     |
| -------------- | --- | --- | ------- | --- | --- | --- |
\qformat{\textbf{Question \thequestion}\quad (\thepoints)\hfill}
| then you’ll | get   |         |     |     |     |     |
| ----------- | ----- | ------- | --- | --- | --- | --- |
| Question    | 1 (10 | points) |     |     |     |     |
What did Billy Joe MacAllister throw off the Tallahatchie Bridge?
| If you instead  | use | the      | command |                    |     |               |
| --------------- | --- | -------- | ------- | ------------------ | --- | ------------- |
| \qformat{\hfill |     | Question |         | \thequestion\hfill |     | (\thepoints)} |
| then you’ll     | get |          |         |                    |     |               |
|                 |     |          |         | Question           | 1   | (10 points)   |
What did Billy Joe MacAllister throw off the Tallahatchie Bridge?
If you use a \qformat (and, if there are any bonus questions, also a \bonusqformat; see
section 4.6), so that there are no labels on any of the questions, and you’d like to remove
| the indentation |     | of the | questions, | you | should give | the command |
| --------------- | --- | ------ | ---------- | --- | ----------- | ----------- |
\renewcommand{\questionshook}{%
\setlength{\leftmargin}{0pt}%
\setlength{\labelwidth}{-\labelsep}%
}
| (see section | 4.10) | before | the questions |     | environment. |     |
| ------------ | ----- | ------ | ------------- | --- | ------------ | --- |
| 4.4.1 Adding |       | up     | the points    | for | a question   |     |
You can combine \qformat with the \totalpoints command (see section 4.3.9): If you
assignpointsonlytoparts, subparts, andsubsubpartsofquestions, butnonetothequestions
| themselves, | and | you give | the | command |     |     |
| ----------- | --- | -------- | --- | ------- | --- | --- |
\qformat{Question \thequestion\dotfill \emph{\totalpoints\ points}}
(youmusthaveusedthedocumentclassoptionaddpointsorgiventhecommand\addpoints
in order to use the \totalpoints command; see section 3.1), then you can type
\begin{questions}
\question
\begin{parts}
\part[10]
In no more than one paragraph, explain why the earth is round.
\part[10]
What changes to the van Allen radiation belt are needed to make
| the | earth | into | a regular | icosahedron? |     |     |
| --- | ----- | ---- | --------- | ------------ | --- | --- |
\end{parts}
\end{questions}
Page 33

| and you’ll | get |     |     |     |
| ---------- | --- | --- | --- | --- |
Question 1 ...................................................................... 20 points
(a) (10 points) In no more than one paragraph, explain why the earth is round.
(b) (10 points) What changes to the van Allen radiation belt are needed to make the
|     | earth into | a regular icosahedron? |     |     |
| --- | ---------- | ---------------------- | --- | --- |
Foranothermethodofprintingthetotalpointsforaquestion, seethe\droptotalpoints
| command | in section       | 4.3.9. |     |     |
| ------- | ---------------- | ------ | --- | --- |
| 4.5     | Titled questions |        |     |     |
The \titledquestion command (see section 4.5.1) allows you to assign a title to a question,
and to have the question title replace the question number in a grading table or point table
indexedbyquestionnumber(seesections9.1and9.2). Ifyouusea\qformat(seesection4.4)
then you can include the question title in the question by using the \thequestiontitle
| command | (see the        | example in section | 4.5.2). |     |
| ------- | --------------- | ------------------ | ------- | --- |
| 4.5.1   | \titledquestion |                    |         |     |
The command \titledquestion is a replacement for \question; it takes one required
argument, the title, and one optional argument, the point value, as in
|     |     | \titledquestion{Question | \thequestion: | Concepts} |
| --- | --- | ------------------------ | ------------- | --------- |
which sets the question title to “Question 2: Concepts” (if this is the second question) and
| doesn’t | set any point | values, or |     |     |
| ------- | ------------- | ---------- | --- | --- |
\titledquestion{Design}[10]
which sets the question title to “Design” and sets the point value to “10”. Note that the
question title doesn’t include the number of the question unless you put it there using the
| \thequestion | command. |     |     |     |
| ------------ | -------- | --- | --- | --- |
Using \titledquestion instead of \question doesn’t change the appearance of the
question (unless you use \thequestiontitle in the argument of a \qformat command; see
section 4.5.2). The only direct effect of using \titledquestion instead of \question is that
if you print a grading table or point table indexed by question number (see section 9.1), then
the title of the question will replace the number of the question in the table. To have the
title of the question appear in the question itself, see the example in section 4.5.2.
If you create a grading table or point table indexed by question number and you create
a question using the \titledquestion command, then the number of the question won’t
appear in the table unless you include \thequestion in the title of the question.
Page 34

| 4.5.2       | \thequestiontitle |     |         |     |     |     |
| ----------- | ----------------- | --- | ------- | --- | --- | --- |
| The command | \thequestiontitle |     | expands | to  |     |     |
• the title of the question (if the question was defined using a \titledquestion com-
| mand) | or  |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- |
•
the number of the question (if the question was defined using a \question command).
This is for use in the argument of a \qformat command (see section 4.4), so that you can
have the question title appear in the question itself, and not just in a grading table or point
table.
The contents of don’t appear anywhere in the question itself unless
\thequestiontitle
you do something to make them appear. For example, if you give the command
\qformat{Question \thequestion: \thequestiontitle\dotfill\thepoints}
| and then | type |     |     |     |     |     |
| -------- | ---- | --- | --- | --- | --- | --- |
\begin{questions}
| \titledquestion{History |     | of  | Empirical | Aerodynamics}[10] |     |     |
| ----------------------- | --- | --- | --------- | ----------------- | --- | --- |
What did Billy Joe MacAllister throw off the Tallahatchie Bridge?
\end{questions}
| then you’ll | get |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- |
Question 1: History of Empirical Aerodynamics..................................10 points
What did Billy Joe MacAllister throw off the Tallahatchie Bridge?
If the command \thequestiontitle is never used, then the only effect of using the
command \titledquestion instead of the command \question is that, in a grading table
or point table indexed by question number, this question will be indexed by the title of the
question rather than by the question number, and the title of the question will never appear
| except | in the table. |     |     |     |     |     |
| ------ | ------------- | --- | --- | --- | --- | --- |
| 4.6    | Bonus points  |     |     |     |     |     |
It’s possible to create questions, parts, subparts, or subsubparts that are worth bonus points,
| instead | of regular points.   | To do | this, you use | the command |                  |     |
| ------- | -------------------- | ----- | ------------- | ----------- | ---------------- | --- |
|         | \bonusquestion       |       |               | instead of  | \question,       |     |
|         | \bonustitledquestion |       |               | instead of  | \titledquestion, |     |
|         | \bonuspart           |       |               | instead of  | \part,           |     |
|         | \bonussubpart        |       |               | instead of  | \subpart,        | and |
|         | \bonussubsubpart     |       |               | instead of  | \subsubpart.     |     |
|         |                      |       | Page          | 35          |                  |     |

There is also a \bonusqformat command that affects the \bonusquestion command in the
same way that the \qformat command affects the \question command (see section 4.4),
and a \nobonusqformat command that cancels the effect of \bonusqformat in the same
way that \noqformat cancels the effect of \qformat. Note that the command \thepoints
is defined so that it works equally well in \qformat and \bonusqformat commands (see
section 4.4).
If you don’t assign any points to a \bonusquestion, \bonuspart, \bonussubpart, or
\bonussubsubpart then, aside from the fact that \bonusqformat alters \bonusquestion
while \qformat alters \question, then they’re printed in the same way that they would
be printed if you had used the corresponding non-bonus command. However, if you assign
points, then
• the points are typeset differently (see below),
• the points are not counted by the \gradetableor \pointtable commands (see
sections 9.1 and 9.2) or their partial variants (see section 9.4), though they are
counted by the \bonusgradetable, \bonuspointtable, \combinedgradetable, and
\combinedpointtable commands and their partial variants (see sections 9.7 and 9.8),
• the points are not counted by the \droptotalpoints command (see section 4.3.9),
though they are counted by the \droptotalbonuspoints command (see below),
• thepointsarenotcountedbythe\pointsofquestion(seesection9.5)or\pointsonpage
(seesection9.6)commands, thoughtheyare countedbythe\bonuspointsofquestion
and \bonuspointsonpage (see section 9.7) commands, and
• the points are not counted by the \numpoints command (see section 4.7), though they
are counted by the \numbonuspoints command (see section 4.7).
The default setup is that if you type
\begin{questions}
\question[10] Who discovered America?
\bonusquestion[1] On what day of the week did he do it?
\bonusquestion[2] What color shirt was he wearing?
\end{questions}
then you’ll get
1. (10 points) Who discovered America?
2. (1 point (bonus)) On what day of the week did he do it?
3. (2 points (bonus)) What color shirt was he wearing?
There is also a command \bonuspointpoints that is analogous to \pointpoints (see
section 4.3.5); the default setup was created by the command
Page 36

|       |                        |               | \bonuspointpoints{point |            |          |          | (bonus)}{points |        | (bonus)}          |     |
| ----- | ---------------------- | ------------- | ----------------------- | ---------- | -------- | -------- | --------------- | ------ | ----------------- | --- |
| and   | if you                 | give          | the command             |            |          |          |                 |        |                   |     |
|       |                        |               | \bonuspointpoints{bonus |            |          |          | point}{bonus    |        | points}           |     |
| then  | typing                 | the           | above                   | would      | produce  |          |                 |        |                   |     |
| 1.    | (10 points)            |               | Who                     | discovered | America? |          |                 |        |                   |     |
| 2.    | (1 bonus               | point)        |                         | On what    | day of   | the week | did he          | do it? |                   |     |
| 3.    | (2 bonus               | points)       |                         | What color | shirt    | was      | he wearing?     |        |                   |     |
| There | are                    | also commands |                         |            |          |          |                 |        |                   |     |
|       | \bonuspointname        |               |                         | and        |          |          |                 |        | \pointname        | and |
|       |                        |               |                         |            |          | that     | are analogous   | to     |                   |     |
|       | \marginbonuspointname  |               |                         |            |          |          |                 |        | \marginpointname  |     |
| (see  | section                | 4.3.5),       | and                     | commands   |          |          |                 |        |                   |     |
|       | \droptotalbonuspoints, |               |                         |            |          |          |                 |        | \droptotalpoints, |     |
\bonustotalformat, and that are analogous to \totalformat, and
|      | \totalbonuspoints |         |     |               |     |     |        |     | \totalpoints |     |
| ---- | ----------------- | ------- | --- | ------------- | --- | --- | ------ | --- | ------------ | --- |
| (see | section           | 4.3.9). |     |               |     |     |        |     |              |     |
| 4.7  | Counting          |         |     | the questions |     | and | adding | up  | the points   |     |
Theexamdocumentclassautomaticallycountsthenumbersofquestions,parts,andsubparts,
| and | makes | these | numbers | available |     | as the | macros |     |     |     |
| --- | ----- | ----- | ------- | --------- | --- | ------ | ------ | --- | --- | --- |
\numquestions
\numparts
\numsubparts
\numsubsubparts
These numbers are also printed on the screen when you run LATEX and they are placed into
the .log file as well. If you have more than one questions environment (for example, if
your exam has several parts, with the questions in each part numbered beginning with “1”),
then \numquestions will hold the total number of questions on the exam. If you do have
more than one questions environment, though, you won’t be able to use the \gradetable
| or  | \pointtable |     | commands | (see | section | 9). |     |     |     |     |
| --- | ----------- | --- | -------- | ---- | ------- | --- | --- | --- | --- | --- |
If you use the document class option or give the command (see
|     |     |     |     |     |     | addpoints |     |     |     | \addpoints |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ---------- |
section 3.1), then the class will add the total number of points and the total number of
bonus points (see section 4.6) that you’ve given to all of the questions, parts, subparts, and
subsubparts of the exam, and make those totals available in the macros
\numpoints
\numbonuspoints
|     |     |     |     |     |     | Page | 37  |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |

as well as displaying those totals on the screen when you run LATEX and placing them into
| the .log | file. You can | then type |     |     |
| -------- | ------------- | --------- | --- | --- |
\begin{center}
This exam has \numquestions\ questions, for a total of \numpoints\
| points | and \numbonuspoints\ |     | bonus points. |     |
| ------ | -------------------- | --- | ------------- | --- |
\end{center}
| and you’ll | get |     |     |     |
| ---------- | --- | --- | --- | --- |
This exam has 8 questions, for a total of 120 points and 10 bonus points.
Warning: If addpoints is in effect, your point values for questions, parts, subparts,
and subsubparts must not contain anything other than digits and the command \half (see
section 4.3.3). For example, if you don’t give the command \addpoints, then you can type
\question[10\%]
with no problems, but this will cause errors if you’ve given the command \addpoints. The
correct way to accomplish what you want is to give the command \marginpointname{\%}
or \pointname{\%} and then type \question[10] (see section 4.3.5).
If you want to temporarily turn off the adding of points (for example, if you list both the
total points for each question and the points for each part, but you don’t want to count the
| points twice), | you can | give the command |     |     |
| -------------- | ------- | ---------------- | --- | --- |
\noaddpoints
to turn off the adding of points and the command \addpoints to turn it back on.
If addpoints is in effect, then you can create grading tables (see section 9.1) and point
tables (see section 9.2) and use the commands \pointsofquestion (see section 9.5) and
| \pointsonpage | (see | section 9.6). |     |     |
| ------------- | ---- | ------------- | --- | --- |
4.8 Referring to specific questions by number (cross references)
You can use the standard LATEX commands and to refer to questions (or parts,
|     |     |     | \label | \ref |
| --- | --- | --- | ------ | ---- |
or subparts, or subsubparts) by number. For example, if you type
| The first              | question                 | is question | number~\ref{ques:first}.          |             |
| ---------------------- | ------------------------ | ----------- | --------------------------------- | ----------- |
| Question               | number~\ref{ques:second} |             | has both                          | a good part |
| (part~\ref{part:good}) |                          | and         | a bad part (part~\ref{part:bad}). |             |
\begin{questions}
\question
\label{ques:first}
| This is | the first | question. |     |     |
| ------- | --------- | --------- | --- | --- |
\question
|     |     |     | Page 38 |     |
| --- | --- | --- | ------- | --- |

\label{ques:second}
\begin{parts}
\part
\label{part:good}
| This is | the good | part. |     |     |     |     |
| ------- | -------- | ----- | --- | --- | --- | --- |
\part
\label{part:bad}
| This is | the \emph{bad} | part. |     |     |     |     |
| ------- | -------------- | ----- | --- | --- | --- | --- |
\end{parts}
\question
| Is there | a question? |     |     |     |     |     |
| -------- | ----------- | --- | --- | --- | --- | --- |
\end{questions}
| then you’ll | get: |     |     |     |     |     |
| ----------- | ---- | --- | --- | --- | --- | --- |
Thefirstquestionis questionnumber 1. Questionnumber2 has bothagoodpart(parta)
| and a bad   | part (part   | b).        |     |     |     |     |
| ----------- | ------------ | ---------- | --- | --- | --- | --- |
| 1. This     | is the first | question.  |     |     |     |     |
| 2. (a)      | This is the  | good part. |     |     |     |     |
| (b)         | This is the  | bad part.  |     |     |     |     |
| 3. Is there | a question?  |            |     |     |     |     |
As with all other cross references in LATEX, you’ll have to run your file through LATEX
| twice to    | be sure that | all the cross | references | are correct.  |         |     |
| ----------- | ------------ | ------------- | ---------- | ------------- | ------- | --- |
| 4.9         | Customizing  | the           | numbers    |               |         |     |
| The default | setup        | is that:      |            |               |         |     |
| 1. Question | numbers      | are arabic,   | and are    | followed by a | period. |     |
(a) Part numbers are lower case letters, and are enclosed in parentheses.
i. Subpart numbers are lower case roman, and are followed by a period.
?) Subsubpart numbers are greek, and are followed by a right parenthesis.
|             |        | A. Choices | are upper | case letters, | and are followed | by a period. |
| ----------- | ------ | ---------- | --------- | ------------- | ---------------- | ------------ |
| All of this | can be | changed.   |           |               |                  |              |
To change the type of numbering, you would redefine the commands
|     |     |     |     | Page 39 |     |     |
| --- | --- | --- | --- | ------- | --- | --- |

\thequestion
\thepartno
\thesubpart
\thesubsubpart
\thechoice
(Note: The second one listed there is \thepartno, not \thepart. The command \thepart
referstothecounterusedinthearticledocumentclassstandardsectioningcommand\part.)
| The numbering | commands | available | are           |                 |
| ------------- | -------- | --------- | ------------- | --------------- |
|               |          | \arabic   | Regular       | arabic integers |
|               |          | \alph     | Lower case    | letters         |
|               |          | \Alph     | Upper case    | letters         |
|               |          | \roman    | Lower case    | roman numbers   |
|               |          | \Roman    | Upper case    | roman numbers   |
|               |          | \greeknum | Greek letters |                 |
and any of these can be applied to the countersquestion, partno, subpart, subsubpart,
and choice. (The \greeknum command is defined by the exam document class, but all of
| the others | are standard | LATEX commands.) |     |     |
| ---------- | ------------ | ---------------- | --- | --- |
For example, to have questions numbered using upper case roman numbers and parts
numbered using upper case letters, you would give the commands
\renewcommand{\thequestion}{\Roman{question}}
\renewcommand{\thepartno}{\Alph{partno}}
The “decorations” around the numbers (i.e., the periods, or parentheses, or ...) are
| determined | by the | commands |     |     |
| ---------- | ------ | -------- | --- | --- |
\questionlabel
\partlabel
\subpartlabel
\subsubpartlabel
\choicelabel
| the default | definitions | of which are: |     |     |
| ----------- | ----------- | ------------- | --- | --- |
\newcommand{\questionlabel}{\thequestion.}
\newcommand{\partlabel}{(\thepartno)}
\newcommand{\subpartlabel}{\thesubpart.}
\newcommand{\subsubpartlabel}{\thesubsubpart)}
\newcommand{\choicelabel}{\thechoice.}
You can change any of these by giving \renewcommand commands to redefine them. This
can, of course, be used to change the “decorations” around the numbers, but there are other
uses as well. For example, if you use the Fourier project’s Utopia font by including the
commands
|     |     |     | Page | 40  |
| --- | --- | --- | ---- | --- |

\usepackage[T1]{fontenc}
\usepackage{fourier}
after your \documentclass command, then you’ll see that the kerning makes “F.” look so
much like “E” that a student could confuse the two. You can turn off the kerning with the
| command |             | \renewcommand{\choicelabel}{\thechoice{}.}. |     |     |                 |     |     |     |     |
| ------- | ----------- | ------------------------------------------- | --- | --- | --------------- | --- | --- | --- | --- |
| 4.10    | Customizing |                                             |     | the | list parameters |     |     |     |     |
The environments questions, parts, subparts, subsubparts, choices, and checkboxes
are all implemented as LATEX list environments. This section describes commands for
advanceduserswhowanttocustomizethelistparameters(\topsep, \partopsep, \itemsep,
| \parsep, |                  | etc.) for | the lists | that           | those environments |           | create.     |              |     |
| -------- | ---------------- | --------- | --------- | -------------- | ------------------ | --------- | ----------- | ------------ | --- |
|          | The exam         | document  |           | class includes | the                | expansion | of          |              |     |
|          | \questionshook   |           |           | when           | creating           | a         | questions   | environment, |     |
|          | \partshook       |           |           | when           | creating           | a         | parts       | environment, |     |
|          | \subpartshook    |           |           | when           | creating           | a         | subparts    | environment, |     |
|          | \subsubpartshook |           |           | when           | creating           | a         | subsubparts | environment, |     |
|          | \choiceshook     |           |           | when           | creating           | a         | choices     | environment, | and |
|          | \checkboxeshook  |           |           | when           | creating           | a         | checkboxes  | environment. |     |
| The      | exam             | document  | class     | defines        | these as           | follows:  |             |              |     |
\newcommand{\questionshook}{}
\newcommand{\partshook}{}
\newcommand{\subpartshook}{}
\newcommand{\subsubpartshook}{}
\newcommand{\choiceshook}{}
\newcommand{\checkboxeshook}{}
Thus, the default is that these commands have no effect, but you can change any of them
with a \renewcommand command. Thus, if you redefine, e.g., \questionshook to expand to
commands that set values for some of the list parameters, then those values will be used in
| the | questions    | environment. |        |          |         |     |     |     |     |
| --- | ------------ | ------------ | ------ | -------- | ------- | --- | --- | --- | --- |
|     | For example, |              | if you | give the | command |     |     |     |     |
\renewcommand{\questionshook}{\setlength{\itemsep}{1in}}
then there will be an additional one inch of blank space inserted between questions (since
the questions are the items in a questions environment). For another example, if you give
the command
\renewcommand{\partshook}{\setlength{\topsep}{0.5in}}
then each parts environment will have an additional one half inch of space before and after
the environment.
For another example, if you’re using a \qformat (see section 4.4) (and, if there are any
bonus questions, also a \bonusqformat; see section 4.6), so that there are no labels on any of
the questions, and you’d like to remove the indentation of the questions, give the command
Page 41

\renewcommand{\questionshook}{%
\setlength{\leftmargin}{0pt}%
\setlength{\labelwidth}{-\labelsep}%
}
| 5   | Multiple |     |     | choice | and | fill | in the | blank | questions |
| --- | -------- | --- | --- | ------ | --- | ---- | ------ | ----- | --------- |
There are four environments for listing the possible answers to a multiple choice question:
two of them label the choices, and the other two print checkboxes in front of the choices for
| the | student | to  | place | checks | next to | the chosen | answers. |     |     |
| --- | ------- | --- | ----- | ------ | ------- | ---------- | -------- | --- | --- |
• The first two environments use upper case letters (i.e., “A”, “B”, “C”, ...) to label
the choices. (To change the appearance of the labels, see section 4.9.)
– The choices environment creates a list environment with the choices as the items
|     |     | in the | list | (see section | 5.1). |     |     |     |     |
| --- | --- | ------ | ---- | ------------ | ----- | --- | --- | --- | --- |
– The oneparchoices environment lists all of the choices in a single paragraph
which is a continuation of the paragraph preceding the environment unless you
leave a blank line before beginning the environment (see section 5.2).
If you don’t want the students to just circle the correct choices, you can use the
\answerline command to print a line on which the answer should be written (see
section 7.6). The \anwerline command allows you to include as an optional argument
the answer to the question, and the answer will be printed on the line when solutions
|     | are | bing | printed | (see | section 7.7). |     |     |     |     |
| --- | --- | ---- | ------- | ---- | ------------- | --- | --- | --- | --- |
• The last two environments print checkboxes in front of the choices for the students to
|     | use | to place | checks | next | to the | chosen | answers. |     |     |
| --- | --- | -------- | ------ | ---- | ------ | ------ | -------- | --- | --- |
– The checkboxes environment creates a list environment with the choices as the
|     |     | items | in the | list | (see section | 5.3). |     |     |     |
| --- | --- | ----- | ------ | ---- | ------------ | ----- | --- | --- | --- |
– The oneparcheckboxes environment lists all of the choices in a single paragraph
which is a continuation of the paragraph preceding the environment unless you
leave a blank line before beginning the environment (see section 5.4).
All of those environments allow you to designate one or more choices as correct choices
and to have the correct choices printed with emphasis when solutions are being printed (see
section 5.5).
| 5.1 |          | The choices |     | environment |     |     |         |     |     |
| --- | -------- | ----------- | --- | ----------- | --- | --- | ------- | --- | --- |
| For | example, | if          | you | type        |     |     |         |     |     |
|     |          |             |     |             |     |     | Page 42 |     |     |

\begin{questions}
\question
One of these things is not like the others; one of these things is not
| the same. | Which one | is different? |
| --------- | --------- | ------------- |
\begin{choices}
| \choice | John |     |
| ------- | ---- | --- |
| \choice | Paul |     |
\choice
George
| \choice | Ringo    |     |
| ------- | -------- | --- |
| \choice | Socrates |     |
\end{choices}
\end{questions}
| Then you’ll | get |     |
| ----------- | --- | --- |
1. One of these things is not like the others; one of these things is not the same. Which
| one | is different? |     |
| --- | ------------- | --- |
A. John
B. Paul
C. George
D. Ringo
E. Socrates
As that example illustrates, you can leave blank lines between the \choice command and
the text of the choice, or between the various choices, and those blank lines will be ignored.
| 5.2 | The oneparchoices | environment |
| --- | ----------------- | ----------- |
If you use a oneparchoices environment instead of the choices environment in the example
| of section | 5.1, then you’ll | get |
| ---------- | ---------------- | --- |
1. One of these things is not like the others; one of these things is not the same. Which
one is different? A. John B. Paul C. George D. Ringo E. Socrates
If you insert a blank line before the \begin{oneparchoices}, then you’ll get
Page 43

1. One of these things is not like the others; one of these things is not the same. Which
| one     | is different?  |      |           |                       |             |             |       |
| ------- | -------------- | ---- | --------- | --------------------- | ----------- | ----------- | ----- |
| A. John | B. Paul        |      | C. George | D. Ringo              | E. Socrates |             |       |
| If you  | insert a blank | line | before    | the                   |             | and         | after |
|         |                |      |           | \begin{oneparchoices} |             | \answerline |       |
the \end{oneparchoices} (see section 7.6 for a description of the \answerline command),
| then you’ll | get |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- |
1. One of these things is not like the others; one of these things is not the same. Which
| one     | is different? |     |           |          |             |     |     |
| ------- | ------------- | --- | --------- | -------- | ----------- | --- | --- |
| A. John | B. Paul       |     | C. George | D. Ringo | E. Socrates |     |     |
1.
| 5.3 The | checkboxes |     | environment |     |     |     |     |
| ------- | ---------- | --- | ----------- | --- | --- | --- | --- |
If you use a checkboxes environment instead of the choices environment in the example of
| section 5.1, | then you’ll | get |     |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- | --- | --- |
1. One of these things is not like the others; one of these things is not the same. Which
| one | is different? |     |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | --- | --- | --- |
(cid:13) John
(cid:13) Paul
(cid:13) George
(cid:13) Ringo
(cid:13) Socrates
The appearance of the checkbox can be customized (see section 5.7).
| 5.4 The |     |     |     | environment |     |     |     |
| ------- | --- | --- | --- | ----------- | --- | --- | --- |
oneparcheckboxes
If you use a oneparcheckboxes environment instead of the choices environment in the
| example | of section 5.1, | then | you’ll get |     |     |     |     |
| ------- | --------------- | ---- | ---------- | --- | --- | --- | --- |
1. One of these things is not like the others; one of these things is not the same. Which
one is different? (cid:13) John (cid:13) Paul (cid:13) George (cid:13) Ringo (cid:13) Socrates
If you insert a blank line before the \begin{oneparcheckboxes}, then you’ll get
1. One of these things is not like the others; one of these things is not the same. Which
| one           | is different? |     |                 |                |                   |     |     |
| ------------- | ------------- | --- | --------------- | -------------- | ----------------- | --- | --- |
| (cid:13) John | (cid:13) Paul |     | (cid:13) George | (cid:13) Ringo | (cid:13) Socrates |     |     |
The appearance of the checkbox can be customized (see section 5.7).
Page 44

5.5 Solutions to multiple choice questions
The exam document class defines several environments for solutions (see section 8), the
contents of which will be printed only if you use the document class option answers (as in
\documentclass[answers]{exam}) or give the command \printanswers (see section 3.2).
Each of the environments for multiple choice questions (see sections 5.1–5.4) allows you to
designateoneormoreofthechoicesascorrect choices, andtohavethecorrectchoicesprinted
with emphasis when solutions are being printed.
The command to define a correct choice is \CorrectChoice, which is used in place of
the command \choice. (To avoid confusion, \correctchoice is defined to be a synonym
for \CorrectChoice.) When solutions are not being printed, \CorrectChoice is equivalent
to \choice. When solutions are being printed, though, any choices that were created with
\CorrectChoice (rather than with \choice) will be printed in bold. (This can be changed;
see section 5.7.) In addition, in the checkboxes and oneparcheckboxes environments, each
correct choice will have its checkbox replaced by a check.
For example, if \printanswers is in effect and you type
\begin{questions}
\question One of these things is not like the others; one of these
things is not the same. Which one is different?
\begin{oneparchoices}
\choice John
\choice Paul
\choice George
\choice Ringo
\CorrectChoice Socrates
\end{oneparchoices}
\end{questions}
then you’ll get
1. One of these things is not like the others; one of these things is not the same. Which
one is different? A. John B. Paul C. George D. Ringo E. Socrates
If you use a oneparcheckboxes environment instead of the oneparchoices environment in
that example, then you’ll get
1. One of these things is not like the others; one of these things is not the same. Which
?
one is different? (cid:13) John (cid:13) Paul (cid:13) George (cid:13) Ringo Socrates
5.6 Fill in the blank questions
There is a \fillin command that prints underlined empty space for creating “fill in the
blank” questions. The \fillin command can take two optional arguments:
• the first optional argument is the answer to the question, which will be printed above
the line when answers are being printed, and
Page 45

•
the second optional argument is the length of line to be printed, if you want some
| length | other than | the | default. |     |     |
| ------ | ---------- | --- | -------- | --- | --- |
If answers are being printed and you supply the answer as the first (and possibly only)
optional argument, then the answer is printed subject to the declarations in the argument of
the most recent \CorrectChoiceEmphasis command. It is centered on the line unless it is
too long, in which case it extends to the right of the line. The default length of the line and
the distance down from the baseline of the text to the empty line can both be customized
| (see section | 5.6.2). |      |     |     |     |
| ------------ | ------- | ---- | --- | --- | --- |
| For example, | if you  | type |     |     |     |
\begin{questions}
| \question | \fillin | is  | the color | of my true | love’s hair. |
| --------- | ------- | --- | --------- | ---------- | ------------ |
\end{questions}
| then you’ll  | get      |       |       |                   |     |
| ------------ | -------- | ----- | ----- | ----------------- | --- |
| 1.           | is the   | color | of my | true love’s hair. |     |
| If, instead, | you type |       |       |                   |     |
\begin{questions}
\question \fillin[Black] is the color of my true love’s hair.
\end{questions}
| then if answers | are not   | being     | printed | you’ll get        |              |
| --------------- | --------- | --------- | ------- | ----------------- | ------------ |
| 1.              | is        | the color | of my   | true love’s hair. |              |
| and if answers  | are being | printed   | you’ll  | get               |              |
| 1. Black        | is        | the color | of my   | true love’s hair. |              |
| For another     | example,  | if        | answers | are being printed | and you type |
\begin{questions}
| \question | The magic |     | word is | \fillin[prestidigitator]. |     |
| --------- | --------- | --- | ------- | ------------------------- | --- |
\end{questions}
| then you’ll  | get     |                  |     |     |     |
| ------------ | ------- | ---------------- | --- | --- | --- |
| 1. The magic | word is | prestidigitator. |     |     |     |
which shows what happens when the answer is too long for the fillin line. If, however, you
type
\begin{questions}
| \question | The magic |     | word is | \fillin[prestidigitator][2in]. |     |
| --------- | --------- | --- | ------- | ------------------------------ | --- |
\end{questions}
|     |     |     |     | Page 46 |     |
| --- | --- | --- | --- | ------- | --- |

| then | you’ll | get   |      |     |                 |     |     |     |     |     |
| ---- | ------ | ----- | ---- | --- | --------------- | --- | --- | --- | --- | --- |
| 1.   | The    | magic | word | is  | prestidigitator |     |     | .   |     |     |
\fillineats(andignores)spacecharactersappearingbeforethefirstoptionalargument.
It also eats (and ignores) space characters appearing after the first optional argument and
before the second optional argument. However, if exactly one optional argument appears,
and if there are one or more space characters following that one optional argument, then
those spaces are replaced by a single space character, but not eaten.
| 5.6.1 | True/False |     |     | questions |     |     |     |     |     |     |
| ----- | ---------- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
The \fillin command can also be used to create True/False questions. If you give the
command
\newcommand{\tf}[1][{}]{%
\fillin[#1][0.25in]%
}
| then | you | can | type |     |     |     |     |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
\begin{questions}
|     | \question |     | \tf[T] | The | world    | is    | all that | is       | the case. |     |
| --- | --------- | --- | ------ | --- | -------- | ----- | -------- | -------- | --------- | --- |
|     | \question |     | \tf[F] | My  | favorite | color |          | is blue. |           |     |
\end{questions}
| and   | if answers  |           | are not   | being       | printed        | you’ll      | get    |          |     |     |
| ----- | ----------- | --------- | --------- | ----------- | -------------- | ----------- | ------ | -------- | --- | --- |
| 1.    | The         | world     |           | is all that | is the         | case.       |        |          |     |     |
| 2.    | My          | favorite  |           | color       | is blue.       |             |        |          |     |     |
| but   | if answers  |           | are being | printed     |                | then you’ll | get    |          |     |     |
| 1.    | T The       | world     |           | is all that | is the         | case.       |        |          |     |     |
| 2.    | F My        | favorite  |           | color       | is blue.       |             |        |          |     |     |
| 5.6.2 | Customizing |           |           | the         | \fillin        | command     |        |          |     |     |
| You   | can         | customize |           | the \fillin |                | command     | by     | changing |     |     |
|       | • the       | default   | length    | of          | the underlined |             | space, |          |     |     |
•
|     | the | distance | below | the | text | baseline | that | the line | is printed, | and |
| --- | --- | -------- | ----- | --- | ---- | -------- | ---- | -------- | ----------- | --- |
•
the emphasis applied to the answer (when answers are being printed).
The default length of the underlined space is called \fillinlinelength, and its value was
| set | by the | command |     |     |     |     |      |     |     |     |
| --- | ------ | ------- | --- | --- | --- | --- | ---- | --- | --- | --- |
|     |        |         |     |     |     |     | Page | 47  |     |     |

\setlength\fillinlinelength{1in}
| You can | change | this | by giving | a   | new | \setlength |     | command. |
| ------- | ------ | ---- | --------- | --- | --- | ---------- | --- | -------- |
The line is printed a distance of below the baseline, and its value was
\answerclearance
| set by | the command |     |     |     |     |     |     |     |
| ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
\setlength\answerclearance{0.2ex}
You can change this by giving a new \setlength command. Note: \answerclearance is
| also used | by  | the \answerline |     | command |     | (see | section | 7.6). |
| --------- | --- | --------------- | --- | ------- | --- | ---- | ------- | ----- |
When answers are being printed and you include the optional argument containing the
answer, then the answer is printed subject to the declarations in the argument of the most
recent \CorrectChoiceEmphasis command. The default situation was created by the com-
mand
\CorrectChoiceEmphasis{\bfseries}
and you can change this by giving a new \CorrectChoiceEmphasis command (see sec-
tion 5.7).
| 5.7 | Customizing |     | the | multiple |     |     | choice | environments |
| --- | ----------- | --- | --- | -------- | --- | --- | ------ | ------------ |
When solutions are being printed, the correct choices in any of the environments choices,
oneparchoices, checkboxes, and oneparcheckboxes will be printed subject to the decla-
| rations | in the | argument | of  | the most | recent |     |     |     |
| ------- | ------ | -------- | --- | -------- | ------ | --- | --- | --- |
\CorrectChoiceEmphasis
| command. | The | default | situation |     | is created |     | by the | command |
| -------- | --- | ------- | --------- | --- | ---------- | --- | ------ | ------- |
\CorrectChoiceEmphasis{\bfseries}
andsowhensolutionsarebeingprintedthecorrectchoicesareprintedinboldfacebydefault.
| You can | change | this, | for example, |     | by  | giving | the command |     |
| ------- | ------ | ----- | ------------ | --- | --- | ------ | ----------- | --- |
\CorrectChoiceEmphasis{\itshape}
which would cause correct choices to be printed in italics when solutions are being printed.
Foranotherexample,ifyougivethecommand\usepackage{color}(or\usepackage{xcolor})
in the preamble of your document (i.e., after the \documentclass command and before the
| \begin{document}), |     |     | and then | give | the | command |     |     |
| ------------------ | --- | --- | -------- | ---- | --- | ------- | --- | --- |
\CorrectChoiceEmphasis{\color{red}}
then when solutions are being printed the correct choices will be printed in red (assuming
| your printer |     | can produce | that | color). |     |     |     |     |
| ------------ | --- | ----------- | ---- | ------- | --- | --- | --- | --- |
Foranotherexample,ifyougivethecommand\usepackage{color}(or\usepackage{xcolor})
in the preamble of your document (i.e., after the \documentclass command and before the
| \begin{document} |     |     | command) | and | then | give | the command |     |
| ---------------- | --- | --- | -------- | --- | ---- | ---- | ----------- | --- |
|                  |     |     |          |     |      | Page | 48          |     |

\CorrectChoiceEmphasis{\color{red}\bfseries}
then the correct choices will be printed in boldface red (again assuming that your printer
| can | produce |     | that color). |     |     |     |     |     |     |
| --- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
To avoid confusion, \correctchoiceemphasis is defined to be a synonym for
\CorrectChoiceEmphasis.
The checkboxes and oneparcheckboxes environments also allow customization of the
| characters |       | used     | for | checkboxes      | and | checks: |            |                  |              |
| ---------- | ----- | -------- | --- | --------------- | --- | ------- | ---------- | ---------------- | ------------ |
|            | • The | checkbox |     | that is printed |     | in the  |            | and              | environments |
|            |       |          |     |                 |     |         | checkboxes | oneparcheckboxes |              |
is the argument of the most recent \checkboxchar command. The default is created
|     | by  | the | command |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
\checkboxchar{$\bigcirc$}
For example, if you give the command \usepackage{amssymb} in the preamble of your
document(i.e.,afterthe\documentclasscommandandbeforethe\begin{document}),
|     | then | the | command |     |     |     |     |     |     |
| --- | ---- | --- | ------- | --- | --- | --- | --- | --- | --- |
\checkboxchar{$\Box$}
|     | will | cause | squares | to be | printed | instead | of circles. |     |     |
| --- | ---- | ----- | ------- | ----- | ------- | ------- | ----------- | --- | --- |
• Thecheckthatisprintedforcorrectchoicesinthecheckboxesandoneparcheckboxes
environments when solutions are being printed is the argument of the most recent
|     | \checkedchar |     |     | command. | The | default | is created | by the command |     |
| --- | ------------ | --- | --- | -------- | --- | ------- | ---------- | -------------- | --- |
\checkedchar{$\surd$}
For example, if you’ve given the command \usepackage{amssymb} in the preamble of
yourdocument(i.e.,afterthe\documentclasscommandandbeforethe\begin{document}),
| then | the | commands |     |     |     |     |     |     |     |
| ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
\checkboxchar{$\Box$}
\checkedchar{$\blacksquare$}
| will | cause | the | example | in section | 5.5 | to appear | as  |     |     |
| ---- | ----- | --- | ------- | ---------- | --- | --------- | --- | --- | --- |
1. One of these things is not like the others; one of these things is not the same. Which
one is different? (cid:3) John (cid:3) Paul (cid:3) George (cid:3) Ringo (cid:4) Socrates
|     |     |     |     |     |     |     | Page 49 |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- |

| 6 Escaping |     |     | the | indentation: |     |     | \uplevel |     | and \fullwidth |
| ---------- | --- | --- | --- | ------------ | --- | --- | -------- | --- | -------------- |
There are two commands provided for printing text with a left margin smaller than the one
currently in effect: \uplevel and \fullwidth. Each of these commands takes one argument
| and typesets |     | the argument |     | with an | altered | left | margin. |     |     |
| ------------ | --- | ------------ | --- | ------- | ------- | ---- | ------- | --- | --- |
The \fullwidth command prints its argument using the full width of the printed region,
temporarilycancelingtheindentationcreatedbythequestionsenvironment(andtheparts,
subparts, and subsubparts environments, if you’re inside any of those). The \uplevel
command prints its argument using the indentation in effect before you entered the current
| innermost | environment. |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
Therearealso twoenvironments, EnvUplevelandEnvFullwidth. TheEnvUplevelenvi-
ronment is similar to the \uplevel command and the EnvFullwidth environment is similar
to the \fullwidth command. The environments have the advantage that you can have
verbatim material inside of the environment, while there cannot be any verbatim material
| in the argument |     | of \uplevel |     | or \fullwidth. |     |     |     |     |     |
| --------------- | --- | ----------- | --- | -------------- | --- | --- | --- | --- | --- |
The main uses for these commands are including instructions for a group of questions
(see section 6.1) and naming the parts of a long exam (see section 6.2), but you can use
| them however |           | you like. |              |     |     |     |       |     |           |
| ------------ | --------- | --------- | ------------ | --- | --- | --- | ----- | --- | --------- |
| 6.1          | Including |           | instructions |     | for | a   | group | of  | questions |
If you are inside of a parts environment and you want to give directions for the next few
parts, then those directions should be indented to the level of the question of which they are
| parts, i.e., | up  | one level. | If  | you type |     |     |     |     |     |
| ------------ | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- |
\begin{questions}
\question
| Why | did you | come | to  | Casablanca? |     |     |     |     |     |
| --- | ------- | ---- | --- | ----------- | --- | --- | --- | --- | --- |
\question
\begin{parts}
\part
| Why, | Oh  | why, Oh | why, | Oh; | why | did I | ever | leave | Ohio? |
| ---- | --- | ------- | ---- | --- | --- | ----- | ---- | ----- | ----- |
\uplevel{The following two parts should be answered in classical
Greek:}
\part
| Why | do  | birds sing? |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
\part
| Why | do  | fools fall |     | in love? |     |     |     |     |     |
| --- | --- | ---------- | --- | -------- | --- | --- | --- | --- | --- |
\end{parts}
\end{questions}
|     |     |     |     |     |     | Page | 50  |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |

| then | you’ll         | get |         |         |             |            |          |              |        |     |
| ---- | -------------- | --- | ------- | ------- | ----------- | ---------- | -------- | ------------ | ------ | --- |
|      | 1. Why did     | you | come    | to      | Casablanca? |            |          |              |        |     |
|      | 2. (a) Why,    |     | Oh why, | Oh      | why,        | Oh; why    | did      | I ever leave | Ohio?  |     |
|      | The following  |     | two     | parts   | should      | be         | answered | in classical | Greek: |     |
|      | (b) Why        | do  | birds   | sing?   |             |            |          |              |        |     |
|      | (c) Why        | do  | fools   | fall    | in love?    |            |          |              |        |     |
| You  | can accomplish |     |         | exactly | the         | same thing | by       | replacing    |        |     |
\uplevel{The following two parts should be answered in classical
Greek:}
by
\begin{EnvUplevel}
The following two parts should be answered in classical Greek:
\end{EnvUplevel}
If you want to give instructions for a group of questions, then the indenting for those
instructions should be to the outer left margin, i.e., up one level. For example, if you type
\begin{questions}
\question
Approximate $\displaystyle \int_0^1 \sin x^2 \, dx$ within $.001$ of
|     | its true | value. |     |     |     |     |     |     |     |     |
| --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
\uplevel{Questions \ref{exact-start} through~\ref{exact-end} should
|     | be evaluated |     |     | completely, |     | not | just | approximated.} |     |     |
| --- | ------------ | --- | --- | ----------- | --- | --- | ---- | -------------- | --- | --- |
\question
\label{exact-start}
|     | $\displaystyle |     |     | \int_0^1 |     | \frac{x^2 | \,  | dx}{\sqrt{1-x^2}}$ |     |     |
| --- | -------------- | --- | --- | -------- | --- | --------- | --- | ------------------ | --- | --- |
\question
|     | $\displaystyle |     |     | \int_0^1 |     | \frac{1}{1+x^2}\, |     | dx$ |     |     |
| --- | -------------- | --- | --- | -------- | --- | ----------------- | --- | --- | --- | --- |
\question
\label{exact-end}
|     | $\displaystyle |     |     | \int_0^{\frac{\pi}{2}} |     |     |     | \sin^3 | x \cos x | \, dx$ |
| --- | -------------- | --- | --- | ---------------------- | --- | --- | --- | ------ | -------- | ------ |
\end{questions}
you’ll get
|     |     |     |     |     |     |     | Page | 51  |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |

(cid:90) 1
| 1.  | Approximate | sinx2dx |     | within | .001 | of its | true value. |     |     |
| --- | ----------- | ------- | --- | ------ | ---- | ------ | ----------- | --- | --- |
0
Questions 2 through 4 should be evaluated completely, not just approximated.
|     | (cid:90) 1 x2dx |     |     |     |     |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2.  | ?               |     |     |     |     |     |     |     |     |
1?x2
0
|     | (cid:90) 1 1 |     |     |     |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.  |              | dx  |     |     |     |     |     |     |     |
1+x2
0
(cid:90) ?
2
| 4.  | sin3xcosxdx |     |     |     |     |     |     |     |     |
| --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
0
| You | can accomplish | exactly | the | same | thing | by  | replacing |     |     |
| --- | -------------- | ------- | --- | ---- | ----- | --- | --------- | --- | --- |
\uplevel{Questions \ref{exact-start} through~\ref{exact-end} should
|     | be evaluated | completely, |     |     | not just | approximated.} |     |     |     |
| --- | ------------ | ----------- | --- | --- | -------- | -------------- | --- | --- | --- |
by
\begin{EnvUplevel}
Questions \ref{exact-start} through~\ref{exact-end} should be
|     | evaluated | completely, |     | not | just | approximated. |     |     |     |
| --- | --------- | ----------- | --- | --- | ---- | ------------- | --- | --- | --- |
\end{EnvUplevel}
If you want to give instructions that use the full width of the page (rather than just going
up one level of indentation), then use the \fullwidth command. For example, if you type
\begin{questions}
\question
| This | is the | first | question. |     |     |     |     |     |     |
| ---- | ------ | ----- | --------- | --- | --- | --- | --- | --- | --- |
\question
\begin{parts}
\part
|     | This is | the first | part. |     |     |     |     |     |     |
| --- | ------- | --------- | ----- | --- | --- | --- | --- | --- | --- |
\part
|     | This is | the second | part. |     |     |     |     |     |     |
| --- | ------- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
\begin{subparts}
\subpart
|     | This            | is a subpart. |       |        |       |         |            |           |          |
| --- | --------------- | ------------- | ----- | ------ | ----- | ------- | ---------- | --------- | -------- |
|     | \fullwidth{When |               | you   | finish | this  | exam,   | you        | should go | back and |
|     | reexamine       | your          | work, |        | both  | on this | exam and   | in your   | life up  |
|     | until           | the day       | of    | this   | exam, | for     | any errors | that you  | may have |
|     |                 |               |       |        |       | Page    | 52         |           |          |

made.}
\subpart
|     | This | is  | another | subpart. |     |     |     |     |     |     |     |
| --- | ---- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
\end{subparts}
\end{parts}
\end{questions}
| then | you’ll   | get     |                 |          |     |     |     |     |     |     |     |
| ---- | -------- | ------- | --------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 1.   | This is  | the     | first question. |          |     |     |     |     |     |     |     |
| 2.   | (a) This | is      | the first       | part.    |     |     |     |     |     |     |     |
|      | (b) This | is      | the second      | part.    |     |     |     |     |     |     |     |
|      |          | i. This | is a            | subpart. |     |     |     |     |     |     |     |
When you finish this exam, you should go back and reexamine your work, both on this exam
and in your life up until the day of this exam, for any errors that you may have made.
|     | ii.             | This | is another |            | subpart. |       |              |        |        |      |          |
| --- | --------------- | ---- | ---------- | ---------- | -------- | ----- | ------------ | ------ | ------ | ---- | -------- |
| You | can accomplish  |      | exactly    | the        | same     | thing | by replacing |        |        |      |          |
|     | \fullwidth{When |      |            | you        | finish   | this  | exam,        | you    | should | go   | back and |
|     | reexamine       |      |            | your work, | both     | on    | this         | exam   | and in | your | life up  |
|     | until           |      | the        | day of     | this     | exam, | for any      | errors | that   | you  | may have |
made.}
by
\begin{EnvFullwidth}
|     | When      |     | you finish |            | this exam, |       | you should |        | go back | and  |          |
| --- | --------- | --- | ---------- | ---------- | ---------- | ----- | ---------- | ------ | ------- | ---- | -------- |
|     | reexamine |     |            | your work, | both       | on    | this       | exam   | and in  | your | life up  |
|     | until     |     | the        | day of     | this       | exam, | for any    | errors | that    | you  | may have |
made.
\end{EnvFullwidth}
| 6.2 | Naming |     | the | parts | of  | a long | exam |     |     |     |     |
| --- | ------ | --- | --- | ----- | --- | ------ | ---- | --- | --- | --- | --- |
There are two ways of naming the parts of a long exam. The first way uses the \fullwidth
and \uplevel commands (see section 6.2.1), and the other way uses the standard \part and
| \section |     | commands |     | (see section | 6.2.2). |     |     |     |     |     |     |
| -------- | --- | -------- | --- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
Page 53

| 6.2.1 Using | \uplevel |     | and | \fullwidth |     |     |     |     |
| ----------- | -------- | --- | --- | ---------- | --- | --- | --- | --- |
To place a section name in the exam, just use a \fullwidth command (see section 6) and
include whatever font changing commands that you want to use. For example, if you type
\begin{questions}
\question
| Is there,         | is  | there | balm          | in Gilead? |             |     |     |     |
| ----------------- | --- | ----- | ------------- | ---------- | ----------- | --- | --- | --- |
| \fullwidth{\Large |     |       | \textbf{Essay |            | questions}} |     |     |     |
\question
Explain how the cooling of matter in the centuries following the big
bang has influenced the British parliamentary system of government.
| \fullwidth{\Large |     |     | \textbf{Laboratory |     |     | questions}} |     |     |
| ----------------- | --- | --- | ------------------ | --- | --- | ----------- | --- | --- |
\question
In the cabinet below your laboratory bench you will find a single
edged razor blade, several C-clamps, and a bottle of whiskey.
| Remove | your | appendix. |     | Do not | suture | until your | work has | been |
| ------ | ---- | --------- | --- | ------ | ------ | ---------- | -------- | ---- |
inspected.
\end{questions}
| then you’ll  | get       |      |     |         |     |     |     |     |
| ------------ | --------- | ---- | --- | ------- | --- | --- | --- | --- |
| 1. Is there, | is there  | balm | in  | Gilead? |     |     |     |     |
| Essay        | questions |      |     |         |     |     |     |     |
2. Explain how the cooling of matter in the centuries following the big bang has influenced
| the British | parliamentary |           |     | system | of government. |     |     |     |
| ----------- | ------------- | --------- | --- | ------ | -------------- | --- | --- | --- |
| Laboratory  |               | questions |     |        |                |     |     |     |
3. In the cabinet below your laboratory bench you will find a single edged razor blade,
several C-clamps, and a bottle of whiskey. Remove your appendix. Do not suture until
| your               | work has | been    | inspected.    |      |             |              |     |     |
| ------------------ | -------- | ------- | ------------- | ---- | ----------- | ------------ | --- | --- |
| You can accomplish |          | exactly | the           | same | thing       | by replacing |     |     |
| \fullwidth{\Large  |          |         | \textbf{Essay |      | questions}} |              |     |     |
by
\begin{EnvFullwidth}
| \Large | \textbf{Essay |     |     | questions} |     |     |     |     |
| ------ | ------------- | --- | --- | ---------- | --- | --- | --- | --- |
\end{EnvFullwidth}
Page 54

and replacing
|     | \fullwidth{\Large |     | \textbf{Laboratory |     |     | questions}} |     |
| --- | ----------------- | --- | ------------------ | --- | --- | ----------- | --- |
by
\begin{EnvFullwidth}
|     | \Large | \textbf{Laboratory |     |     | questions} |     |     |
| --- | ------ | ------------------ | --- | --- | ---------- | --- | --- |
\end{EnvFullwidth}
| 6.2.2 | Using | the | standard | sectioning |     | commands |     |
| ----- | ----- | --- | -------- | ---------- | --- | -------- | --- |
The exam document class is built upon the standard article document class, and so the
sectioning commands used with the article document class can be used here as well. In
particular, you can give the commands \part, \part \part*, \section, and \section*.
The definitions made in exam.cls ensure that if a \part command appears outside of a
parts environment it will be interpreted as a sectioning command, while if it appears inside
of a parts environment it will be interpreted as beginning a new part of a question.
You can give these commands in the middle of a questions environment so as not to
interrupt the numbering of the questions, or you can end a questions environment, give
a sectioning command, and then start a new questions environment (which would reset
the question counter to start again with number 1). If you have more than one questions
environment, though, thenyouwillbeunabletouseanyofthecommandsthatcreategrading
tables or point tables (see section 9) or the commands that change the headers and footers
depending on whether or not a question spans multiple pages (see section 11.9).
If you give any of these commands while inside of a questions environment, then the
section titles will be indented to the same extent that questions are indented unless they are
given as the argument of a \fullwidth or \uplevel command. These commands have the
advantage, however, that the unstarred versions provide automatic numbering of the parts
or sections.
| 7     | Leaving    | space      |              | for      | the answers |         |         |
| ----- | ---------- | ---------- | ------------ | -------- | ----------- | ------- | ------- |
| There | are five   | different  | kinds        | of space | that        | you can | create: |
|       | • Blank    | space (see | section      | 7.1),    |             |         |         |
|       | • an empty | box        | (see section | 7.2),    |             |         |         |
•
|     | space | filled with | lines | (see section | 7.3), |     |     |
| --- | ----- | ----------- | ----- | ------------ | ----- | --- | --- |
•
|     | space | filled with | dotted | lines | (see section | 7.4), | and |
| --- | ----- | ----------- | ------ | ----- | ------------ | ----- | --- |
•
|     | space | filled with | a grid | (see section | 7.5). |     |     |
| --- | ----- | ----------- | ------ | ------------ | ----- | --- | --- |
|     |       |             |        |              | Page  | 55  |     |

You can also create answer lines for short answer questions (see section 7.6). In section 8 we
| describe | five environments |     | for | typing | solutions | to questions: |
| -------- | ----------------- | --- | --- | ------ | --------- | ------------- |
•
solution,
•
solutionorbox,
• solutionorlines,
| • solutionordottedlines, |     |     |     | and |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- |
• solutionorgrid.
Each of those environments can take an optional argument specifying an amount of space
to be created when solutions are not being printed; see section 8.5.
| 7.1 | Leaving | blank | space |     |     |     |
| --- | ------- | ----- | ----- | --- | --- | --- |
To leave blank space on the page for the answer to a question, you should use the \vspace*
command. For example, the command \vspace*{1in} inserts one inch of vertical space
after the line in which it appears. (If it appears in between paragraphs, then it inserts the
space right there.) You can also use the \vspace command, the difference being that space
inserted by \vspace will be deleted if it occurs at the top of a new page, whereas space
| inserted | by \vspace* |     | will never | be  | deleted. |     |
| -------- | ----------- | --- | ---------- | --- | -------- | --- |
If you want to leave all the remaining space on the page blank, you should give the
commands
\vspace*{\stretch{1}}
\newpage
If you want to equally distribute the blank space among several questions on the page,
then just put \vspace*{\stretch{1}} after each of the questions and use \newpage to end
the page. You can also distribute the available space in some other ratio. For example,
to give one of the questions on the page twice as much space as any of the others, put
\vspace*{\stretch{2}} after that question and \vspace*{\stretch{1}} after each of the
others.
You can also leave blank space when solutions are not being printed by using an optional
| argument | with a   | solution | environment; |      | see section | 8.5. |
| -------- | -------- | -------- | ------------ | ---- | ----------- | ---- |
| 7.2      | Printing | an       | empty        | box  |             |      |
| You can  | print an | empty    | box          | with | the command |      |
\makeemptybox{length}
|     |     |     |     |     | Page | 56  |
| --- | --- | --- | --- | --- | ---- | --- |

which prints an empty box of height length whose width equals that of the current line.
That is, the left edge is at the current left margin (which depends on whether we’re in a
question, part, subpart, or subsubpart) and the right edge is at the right margin. (The box
printed by the \makeemptybox command can be printed in color; for that, see section 8.7.)
For example, if you type
\begin{questions}
\question
In no more than one paragraph, explain why the earth is round.
\makeemptybox{1in}
\question
\begin{parts}
\part
What changes to the van Allen radiation belt are needed to make
the earth into a regular icosahedron?
\makeemptybox{1in}
\part
Where should the field generator be constructed if you want one of
the vertices to be located at the Royal Observatory at Greenwich?
\makeemptybox{1in}
\end{parts}
\end{questions}
then you’ll get
1. In no more than one paragraph, explain why the earth is round.
2. (a) What changes to the van Allen radiation belt are needed to make the earth into a
regular icosahedron?
Page 57

(b) Where should the field generator be constructed if you want one of the vertices to
be located at the Royal Observatory at Greenwich?
If you want to fill the remaining space on the page with an empty box, you should give
the commands
\makeemptybox{\stretch{1}}
\newpage
If you want to equally distribute the space for the answers among several questions on the
page, then just put \makeemptybox{\stretch{1}} after each of those questions and use
\newpage to end the page. You can also distribute the available space in some other ratio.
For example, to give one of the questions on the page twice as much space as any of the oth-
ers, put \makeemptybox{\stretch{2}} after that question, \makeemptybox{\stretch{1}}
after each of the others, and use \newpage to end the page.
You can also insert an empty box when solutions are not being printed by including an
optional argument with the solutionoremptybox environment; see section 8.5.
7.3 Printing lined space
You can fill space with lines with the command
\fillwithlines{length}
which fills vertical space of height length with horizontal lines that run the length of the
current line. That is, they extend from the current left margin (which depends on whether
we’re in a question, part, subpart, or subsubpart) to the right margin.
By default, the lines are in black. However, if you give the commands
\usepackage{color}
\colorfillwithlines
(or\usepackage{xcolor}insteadof\usepackage{color})(or\usepackage{xcolor})then
the lines will be in color, by default a light gray. That default color was defined by the
command
Page 58

\definecolor{FillWithLinesColor}{gray}{0.8}
You can change the color by giving a new \definecolor command to redefine the color
FillWithLinesColor.
For example, if you type
\begin{questions}
\question
In no more than one paragraph, explain why the earth is round.
\fillwithlines{1in}
\question
\begin{parts}
\part
What changes to the van Allen radiation belt are needed to make
the earth into a regular icosahedron?
\fillwithlines{1in}
\part
Where should the field generator be constructed if you want one of
the vertices to be located at the Royal Observatory at Greenwich?
\fillwithlines{1in}
\end{parts}
\end{questions}
then you’ll get
1. In no more than one paragraph, explain why the earth is round.
2. (a) What changes to the van Allen radiation belt are needed to make the earth into a
regular icosahedron?
Page 59

(b) Where should the field generator be constructed if you want one of the vertices to
be located at the Royal Observatory at Greenwich?
The distance between the lines is \linefillheight, the default value of which is set
with the command
\setlength\linefillheight{.25in}
That value can be changed by giving a new \setlength command. The thickness of the
lines is \linefillthickness, the default value of which is set with the command
\setlength\linefillthickness{0.1pt}
and that value can also be changed by giving a new \setlength command.
If you want to fill the remaining space on the page with lines, you should give the
commands
\fillwithlines{\stretch{1}}
\newpage
If you want to equally distribute the space for the answers among several questions on the
page, then just put \fillwithlines{\stretch{1}} after each of those questions and use
\newpagetoendthepage. Youcanalsodistributetheavailablespaceinsomeotherratio. For
example, to give one of the questions on the page twice as much space as any of the others,
put \fillwithlines{\stretch{2}} after that question, \fillwithlines{\stretch{1}}
after each of the others, and use \newpage to end the page.
You can also insert lined space when solutions are not being printed by including an
optional argument with the solutionorlines environment; see section 8.5.
7.4 Printing dotted lined space
You can fill space with dotted lines with the command
\fillwithdottedlines{length}
which fills vertical space of height length with dotted horizontal lines that run the length
of the current line. That is, they extend from the current left margin (which depends
on whether we’re in a question, part, subpart, or subsubpart) to the right margin. The
command \fillwithdottedlines is almost identical to the \fillwithlines command (see
section 7.3), except that the lines created are dotted and the distance between the lines
is \dottedlinefillheight. The default value of \dottedlinefillheight is set by the
command
Page 60

\setlength\dottedlinefillheight{.25in}
and that value can be changed by giving a new \setlength command.
By default, the dotted lines are in black. However, if you give the commands
\usepackage{color}
\colorfillwithdottedlines
(or \usepackage{xcolor} instead of \usepackage{color}) then the dotted lines will be in
color, by default a light gray. That default color was defined by the command
\definecolor{FillWithDottedLinesColor}{gray}{0.8}
You can change the color by giving a new \definecolor command to redefine the color
FillWithDottedLinesColor.
For example, if you type
\begin{questions}
\question
In no more than one paragraph, explain why the earth is round.
\fillwithdottedlines{1in}
\question
\begin{parts}
\part
What changes to the van Allen radiation belt are needed to make
the earth into a regular icosahedron?
\fillwithdottedlines{1in}
\part
Where should the field generator be constructed if you want one of
the vertices to be located at the Royal Observatory at Greenwich?
\fillwithdottedlines{1in}
\end{parts}
\end{questions}
then you’ll get
1. In no more than one paragraph, explain why the earth is round.
......................................................................................
......................................................................................
......................................................................................
......................................................................................
Page 61

2. (a) What changes to the van Allen radiation belt are needed to make the earth into a
regular icosahedron?
..................................................................................
..................................................................................
..................................................................................
..................................................................................
(b) Where should the field generator be constructed if you want one of the vertices to
be located at the Royal Observatory at Greenwich?
..................................................................................
..................................................................................
..................................................................................
..................................................................................
If you want to fill the remaining space on the page with dotted lines, you should give the
commands
\fillwithdottedlines{\stretch{1}}
\newpage
If you want to equally distribute the space for the answers among several questions on
the page, then just put \fillwithdottedlines{\stretch{1}} after each question on the
page and use \newpage to end the page. You can also distribute the available space in
some other ratio. For example, to give one of the questions on the page twice as much
space as any of the others, put \fillwithdottedlines{\stretch{2}} after that question,
\fillwithdottedlines{\stretch{1}} after each of the others, and use \newpage to end
the page.
You can also insert dotted lined space when solutions are not being printed by including
an optional argument with the solutionordottedlines environment; see section 8.5.
7.5 Printing space filled with a grid
You can fill space with a grid with the command
\fillwithgrid{length}
which fills vertical space of height length with a grid that runs the length of the current
line. That is, it extends from the current left margin (which depends on whether we’re in a
question, part, subpart, or subsubpart) to the right margin. The default grid size and grid
line thickness were set by the commands
\setlength{\gridsize}{5mm}
\setlength{\gridlinewidth}{0.1pt}
Page 62

You can change either or both of those by giving new \setlength commands. The period of
thegridis\gridsize(bothhorizontallyandvertically). Thatis,thehorizontaldistancefrom
theleftedgeofoneverticallinetotheleftedgeofthenextverticallineis\gridsize, asisthe
verticaldistancefromthetopedgeofonehorizontallinetothetopedgeofthenexthorizontal
line. Thus, each square has outer side length equal to \gridsize+\gridlinewidth.
By default, the created grids are in black. However, if you give the commands
\usepackage{color}
\colorgrids
(or \usepackage{xcolor} instead of \usepackage{color}) then the grids will be in color,
by default a light gray. That default color was defined by the command
\definecolor{GridColor}{gray}{0.8}
You can change the color by giving a new \definecolor command to redefine the color
GridColor.
For example, if you type
\begin{questions}
\question
In no more than one paragraph, explain why the earth is round.
\smallskip\fillwithgrid{1in}
\question
\begin{parts}
\part
What changes to the van Allen radiation belt are needed to make
the earth into a regular icosahedron?
\smallskip\fillwithgrid{1in}
\part
Where should the field generator be constructed if you want one of
the vertices to be located at the Royal Observatory at Greenwich?
\smallskip\fillwithgrid{1in}
\end{parts}
\end{questions}
then you’ll get
1. In no more than one paragraph, explain why the earth is round.
Page 63

2. (a) What changes to the van Allen radiation belt are needed to make the earth into a
regular icosahedron?
(b) Where should the field generator be constructed if you want one of the vertices to
be located at the Royal Observatory at Greenwich?
If you want to fill the remaining space on the page with a grid, you should give the
commands
\fillwithgrid{\stretch{1}}
\newpage
If you want to equally distribute the space for the answers among several questions on the
page, then just put \fillwithgrid{\stretch{1}} after each question on the page and use
\newpage to end the page. You can also distribute the available space in some other ratio.
For example, to give one of the questions on the page twice as much space as any of the oth-
ers, put \fillwithgrid{\stretch{2}} after that question, \fillwithgrid{\stretch{1}}
after each of the others, and use \newpage to end the page.
You can also insert a grid only when solutions are not being printed by including an
optional argument with the solutionorgrid environment; see section 8.5.
7.5.1 Covering every page with a grid
If you’d like every page to be completely covered by a grid, with the exam printed right on
top of that grid, you can do that by using a \fillwithgrid command in the footer. For this,
makesureyou’reusingeither\pagestyle{headandfoot}(thedefault)or\pagestyle{foot}
(see section 11.1), and put the following into your preamble (i.e., after the \documentclass
command and before the \begin{document} command):
Page 64

\usepackage{color}
\colorgrids
\newlength{\scratchlength}
\newcommand{\gridfromfoot}{%
\setlength{\scratchlength}{\textheight}%
\addtolength{\scratchlength}{\baselineskip}%
| \leavevmode\rlap{\vbox |     | to 0pt{% |
| ---------------------- | --- | -------- |
\vss
\fillwithgrid{\scratchlength}%
\vspace*{\footskip}%
| }% vbox |     |     |
| ------- | --- | --- |
}% rlap
}% gridfromfoot
| \footer{\gridfromfoot |     | Math 115} |
| --------------------- | --- | --------- |
{}
| {Page | \thepage\ | of \numpages} |
| ----- | --------- | ------------- |
(You could also use \usepackage{xcolor} instead of \usepackage{color})
| 7.5.2 Printing | graph | paper |
| -------------- | ----- | ----- |
You can also use the \fillwithgrid command to print graph paper:
\documentclass{exam}
\pagestyle{empty}
\begin{document}
\fillwithgrid{\stretch{1}}
\newpage
\fillwithgrid{\stretch{1}}
\end{document}
| 7.6 Short | answer | questions |
| --------- | ------ | --------- |
The exam class can print answer lines for short answer questions. The command
\answerline
leaves blank vertical space of length \answerskip and then inserts a horizontal line of length
\answerlinelength at the right margin, preceded by the number of the current question,
part, subpart, or subsubpart. The default values of \answerskip and \answerlinelength
| are set by the | commands |     |
| -------------- | -------- | --- |
Page 65

\setlength\answerskip{2ex}
\setlength\answerlinelength{1in}
and these can be changed by giving new \setlength commands. If you use the command
\answerline outside of a questions environment, then the number before the line will be
omitted.
| For | example, | if you | type |     |     |     |     |     |
| --- | -------- | ------ | ---- | --- | --- | --- | --- | --- |
\begin{questions}
\question
| Who’s | buried | in  | Grant’s | tomb? |     |     |     |     |
| ----- | ------ | --- | ------- | ----- | --- | --- | --- | --- |
\answerline
\question
| What | was the | color | of  | George | Washington’s |     | white | horse? |
| ---- | ------- | ----- | --- | ------ | ------------ | --- | ----- | ------ |
\answerline
\question
| Which | is heavier: |     | A pound |     | of feathers, |     | or a | pound of lead? |
| ----- | ----------- | --- | ------- | --- | ------------ | --- | ---- | -------------- |
\answerline
\end{questions}
| then you’ll | get    |     |         |       |     |     |     |     |
| ----------- | ------ | --- | ------- | ----- | --- | --- | --- | --- |
| 1. Who’s    | buried | in  | Grant’s | tomb? |     |     |     |     |
1.
| 2. What | was | the color | of George |     | Washington’s | white |     | horse? |
| ------- | --- | --------- | --------- | --- | ------------ | ----- | --- | ------ |
2.
| 3. Which | is heavier: |     | A pound | of  | feathers, | or a pound |     | of lead? |
| -------- | ----------- | --- | ------- | --- | --------- | ---------- | --- | -------- |
3.
| and if you | type |     |     |     |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
\begin{questions}
\question
| Answer | the | following |     | questions | on  | the lines |     | at the right: |
| ------ | --- | --------- | --- | --------- | --- | --------- | --- | ------------- |
\begin{parts}
\part
| Who’s | buried |     | in Grant’s |     | tomb? \answerline |     |     |     |
| ----- | ------ | --- | ---------- | --- | ----------------- | --- | --- | --- |
\part
\begin{subparts}
|     |     |     |     |     | Page | 66  |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- |

\subpart
What light through yonder window breaks? \answerline
\subpart
To be, or not to be; that is the question? \answerline
\end{subparts}
\part
What was the color of George Washington’s white horse? \answerline
\end{parts}
\end{questions}
then you’ll get
1. Answer the following questions on the lines at the right:
(a) Who’s buried in Grant’s tomb?
(a)
(b) i. What light through yonder window breaks?
i.
ii. To be, or not to be; that is the question?
ii.
(c) What was the color of George Washington’s white horse?
(c)
7.7 Printing the answers to short answer questions
The \answerline command can take an optional argument so that you can have the answer
to the question printed on the answer line when answers are being printed (see section 3.2).
When answers are not being printed, the optional argument is ignored.
When answers are being printed, the optional argument is printed subject to the decla-
rations in the argument of the last \CorrectChoiceEmphasis command (which by default
is \bfseries; see section 5.5), and it is printed a distance of \answerclearance above the
line. The default value of \answerclearance is set with the command
\setlength\answerclearance{0.2ex}
and it can be changed with a \setlength command. The optional argument is centered on
the answer line unless it is longer than the line, in which case it extends to the right of the
line.
For example, if you type
Page 67

\begin{questions}
\question Who was the fifth Beatle? \answerline[Murray the K]
\question What is the answer to the ultimate question of life, the
| universe, | and everything? |     | \answerline[42] |     |
| --------- | --------------- | --- | --------------- | --- |
\end{questions}
| and if \noprintanswers |               | (the    | default) is in | effect, you’ll get |
| ---------------------- | ------------- | ------- | -------------- | ------------------ |
| 1. Who                 | was the fifth | Beatle? |                |                    |
1.
2. What is the answer to the ultimate question of life, the universe, and everything?
2.
| while if \printanswers |               | is in effect, | you’ll | get |
| ---------------------- | ------------- | ------------- | ------ | --- |
| 1. Who                 | was the fifth | Beatle?       |        |     |
Murray the K
1.
2. What is the answer to the ultimate question of life, the universe, and everything?
2. 42
8 Solutions
| 8.1 Solution | environments |     |     |     |
| ------------ | ------------ | --- | --- | --- |
There are six environments for typing solutions to the problems. These environments all
allow you to either print the solutions or omit them with a single command. Whether or not
| solutions | are printed | is controlled | by the two | commands |
| --------- | ----------- | ------------- | ---------- | -------- |
\printanswers
\noprintanswers
Using these commands to turn printing of solutions on and off, you can print the solutions
for the entire exam or for only certain parts of it. The default is that solutions are not
printed. There is also an answers option to the exam document class, used as in
\documentclass[answers]{exam}
that is equivalent to giving the command \printanswers at the beginning of the document
| (see section | 3.2).        |               |     |                         |
| ------------ | ------------ | ------------- | --- | ----------------------- |
| The six      | environments | for solutions | are | divided into two types. |
Page 68

•
The solutionbox environment (see section 8.6) always prints a box, of whatever size
you choose, and if solutions are being printed it prints the solution inside of the box.
•
|     | Each of the | remaining |     | five | (see section | 8.5), |              |     |     |
| --- | ----------- | --------- | --- | ---- | ------------ | ----- | ------------ | --- | --- |
|     |             |           | the |      |              |       | environment, |     |     |
solution
|     |     |     | the | solutionorbox         |     |     | environment, |     |     |
| --- | --- | --- | --- | --------------------- | --- | --- | ------------ | --- | --- |
|     |     |     | the | solutionorlines       |     |     | environment, |     |     |
|     |     |     | the | solutionordottedlines |     |     | environment, |     | and |
|     |     |     | the | solutionorgrid        |     |     | environment, |     |     |
by default prints either the solution or nothing at all. However, they all can take one
optional argument, which is an amount of space to be left when solutions are not being
printed. If you use these environments without any optional arguments, then they are
identical: They print either the solution or nothing at all. They differ only in the type
of space they leave when you do include the optional argument and solutions are not
|     | being printed. |     |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
The differences between these five environments are that if the optional argument is
|     | used and | solutions | are | not | being printed, | then |     |     |     |
| --- | -------- | --------- | --- | --- | -------------- | ---- | --- | --- | --- |
– the solution environment inserts that amount of blank space, as if you had given
a \vspace* command (or, if you’ve given the command \unstarredvspace, as if
|     | you | had given | a   | \vspace | command) | (see section |     | 7.1), |     |
| --- | --- | --------- | --- | ------- | -------- | ------------ | --- | ----- | --- |
– the environment inserts an empty box of that height, as if you
solutionorbox
|     | had | given | a \makeemptybox |     | command | (see | section | 7.2), |     |
| --- | --- | ----- | --------------- | --- | ------- | ---- | ------- | ----- | --- |
– the solutionorlines environment inserts that amount of space with ruled lines,
as if you had given a \fillwithlines command (see section 7.3),
– the solutionordottedlines environment inserts that amount of space with dot-
tedlines, asifyouhadgivena\fillwithdottedlinescommand(seesection7.4),
and
– the solutionorgrid environment inserts that amount of space filled with a grid,
|     | as if | you had | given | a \fillwithgrid |     | command |     | (see section | 7.5). |
| --- | ----- | ------- | ----- | --------------- | --- | ------- | --- | ------------ | ----- |
Notethattherearetwocommandsthataffectthespaceinsertedbytheoptionalargument
to a solution environment: The command \unstarredvspace causes any space inserted by
anoptionalargumenttothesolutionenvironmenttobeinsertedusinga\vspacecommand,
instead of the \vspace* command. You can return to having such space inserted using a
| \vspace* | command |     | by giving | the | command | \nounstarredvspace. |     |     |     |
| -------- | ------- | --- | --------- | --- | ------- | ------------------- | --- | --- | --- |
You can use a parts, subparts, or subsubparts environment inside any of the solution
environments without having their points (if any) counted as actual points on the exam. If
there are points assigned to any of these commands inside any of the solution environments,
those points are not added to the points of the question or the points on the page, and do
| not | affect any | gradetables | or  | pointtables. |     |         |     |     |     |
| --- | ---------- | ----------- | --- | ------------ | --- | ------- | --- | --- | --- |
|     |            |             |     |              |     | Page 69 |     |     |     |

| 8.2 | The       | appearance |        | of the | solution |     |
| --- | --------- | ---------- | ------ | ------ | -------- | --- |
| The | solutions | printed    | by the |        |          |     |
solution,
solutionorbox,
solutionorlines,
|     |     |     |     | solutionordottedlines, |     | and |
| --- | --- | --- | --- | ---------------------- | --- | --- |
solutionorgrid
| environments |        | can be            | printed   | either       |             |                  |
| ------------ | ------ | ----------------- | --------- | ------------ | ----------- | ---------------- |
|              | • in a | box (i.e.,        | an \fbox) | (see section | 8.2.1; this | is the default), |
|              | • on a | shaded background |           | (see section | 8.2.2),     | or               |
•
|     | with | no framing | or shading | (see section | 8.2.3). |     |
| --- | ---- | ---------- | ---------- | ------------ | ------- | --- |
In all of these cases, solutions can be broken across pages, and the part on each page will
be boxed or shaded as appropriate. In addition, the \SolutionEmphasis command can
be used to highlight the text of the solution (using, e.g., boldface, or italics, or color); see
section 8.4.2.
| 8.2.1 | Printing | the | solution | in a box |     |     |
| ----- | -------- | --- | -------- | -------- | --- | --- |
Bydefault, thesolutionisprintedinsideofabox(i.e., an\fbox), andifthesolutionisbroken
across pages, then each piece is enclosed in a box. (The box can be printed in color; for that,
see section 8.7.) There is also a \shadedsolutions command to instead have the solution
printed in a \colorbox (i.e., printed on a shaded background); for this, you must load the
color package and your printer must be capable of printing color, or at least grayscale (see
section 8.2.2).
|     | For example, | if  | you type |     |     |     |
| --- | ------------ | --- | -------- | --- | --- | --- |
\begin{questions}
|     | \question | Did | you mutter | something? |     |     |
| --- | --------- | --- | ---------- | ---------- | --- | --- |
\begin{solution}
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore--- While I
nodded, nearly napping, suddenly there came a tapping, As of some
one gently rapping, rapping at my chamber door. ‘‘\,’Tis some
visitor,’’ I muttered, ‘‘tapping at my chamber door--- Only this
|     | and nothing |     | more.’’ |     |     |     |
| --- | ----------- | --- | ------- | --- | --- | --- |
\end{solution}
\end{questions}
Page 70

and you’ve given the command \printanswers or used the document class option answers
| (see section | 3.2), then | you’ll     | get |
| ------------ | ---------- | ---------- | --- |
| 1. Did       | you mutter | something? |     |
Solution: Once upon a midnight dreary, while I pondered, weak and weary, Over
many a quaint and curious volume of forgotten lore— While I nodded, nearly nap-
ping, suddenly there came a tapping, As of some one gently rapping, rapping at my
chamber door. “’Tis some visitor,” I muttered, “tapping at my chamber door—
| Only | this and | nothing | more.” |
| ---- | -------- | ------- | ------ |
The result would be exactly the same if that solution environment were replaced by a
solutionorbox, solutionorlines, solutionordottedlines, or solutionorgrid environ-
ment.
By default, the solution is printed in a box whose width equals that of the text of
the current question (or part, or subpart, or subsubpart). That is, the indentation at
the left of the solution equals the current level of indentation. You can change this by
enclosing the solution, solutionorbox, solutionorlines, solutionordottedlines, or
solutionorgrid environment in the argument of a \fullwidth or \uplevel command, or
inside of a EnvFullwidth or EnvUplevelenvironment (see section 6). For example, if you
type
\begin{questions}
| \question | Did | you mutter | something? |
| --------- | --- | ---------- | ---------- |
\begin{EnvFullwidth}
\begin{TheSolution}
Once upon a midnight dreary, while I pondered, weak and weary,
Over many a quaint and curious volume of forgotten lore--- While
I nodded, nearly napping, suddenly there came a tapping, As of
some one gently rapping, rapping at my chamber door. ‘‘\,’Tis
some visitor,’’ I muttered, ‘‘tapping at my chamber door--- Only
| this | and nothing | more.’’ |     |
| ---- | ----------- | ------- | --- |
\end{TheSolution}
\end{EnvFullwidth}
\end{questions}
and you’ve given the command \printanswers or used the document class option answers,
| then you’ll | get        |            |     |
| ----------- | ---------- | ---------- | --- |
| 1. Did      | you mutter | something? |     |
Page 71

Solution: Once upon a midnight dreary, while I pondered, weak and weary, Over many
aquaintandcuriousvolumeofforgottenlore—WhileInodded, nearlynapping, suddenly
there came a tapping, As of some one gently rapping, rapping at my chamber door. “’Tis
some visitor,” I muttered, “tapping at my chamber door— Only this and nothing more.”
With all of these environments, if solutions are not being printed then the contents of the
environment are ignored. If, however, you include the optional argument (see section 8.5),
then the requested amount of space (blank, lined, or dotted lined) will be inserted when the
| solution    | isn’t printed. |       |          |                  |            |
| ----------- | -------------- | ----- | -------- | ---------------- | ---------- |
| 8.2.2       | Printing       | the   | solution | on a shaded      | background |
| If you load | the            | color | package  | with the command |            |
\usepackage{color}
(or the xcolor package with the command \usepackage{xcolor}) in the preamble of your
document(i.e., afterthe \documentclasscommandand before the \begin{document}com-
| mand), | then you | can | give the | command |     |
| ------ | -------- | --- | -------- | ------- | --- |
\shadedsolutions
This will cause solutions to be printed on a shaded background, which by default is a
light gray. (Most laser printers can at least print grayscale when printing with the cor-
rect driver.) If you want to change the color of the shading, you can do so by redefining the
| color SolutionColor. |     |     | For example, | if you give | the command |
| -------------------- | --- | --- | ------------ | ----------- | ----------- |
\definecolor{SolutionColor}{rgb}{0.8,0.9,1}
then the solutions will be printed on a light blue background (assuming that your printer is
| capable | of producing |     | that color). |     |     |
| ------- | ------------ | --- | ------------ | --- | --- |
If you want to switch back to printing solutions inside of an \fbox, you can do so by
| giving the | command |     |     |     |     |
| ---------- | ------- | --- | --- | --- | --- |
\framedsolutions
| which returns | you      | to the  | default  | situation.      |            |
| ------------- | -------- | ------- | -------- | --------------- | ---------- |
| 8.2.3         | Printing | the     | solution | with no framing | or shading |
| If you give   | the      | command |          |                 |            |
\unframedsolutions
Page 72

then solutions will be printed as normal text, with no framing or shading. If you use this op-
tion,you’llalmostcertainlywanttousethecommand\SolutionEmphasis(seesection8.4.2)
| to  | distinguish | the | solution | from | the surrounding |     | text. |     |
| --- | ----------- | --- | -------- | ---- | --------------- | --- | ----- | --- |
If you want to switch back to printing solutions inside of an \fbox, you can do so by
| giving | the | command |     |     |     |     |     |     |
| ------ | --- | ------- | --- | --- | --- | --- | --- | --- |
\framedsolutions
| which | returns  | you | to the   | default | situation.   |     |     |     |
| ----- | -------- | --- | -------- | ------- | ------------ | --- | --- | --- |
| 8.3   | Imported |     | graphics |         | in solutions |     |     |     |
Graphics can be included inside solution environments using the \includegraphics com-
mand, as long as you’ve given the command in the preamble (i.e.,
\usepackage{graphicx}
after the \documentclass command and before the \begin{document} command).
A problem sometimes arises because many LATEX manuals say that you should put an
\includegraphics command inside of a figure environment, so that it will float to a
convenient place on a page. The problem with this is that floating environments can’t
| appear | inside | of a | solution | environment. |     |     |     |     |
| ------ | ------ | ---- | -------- | ------------ | --- | --- | --- | --- |
There are (at least) two solutions to this problem, depending on whether you really want
the graphic to float away from the location at which you’ve typed it.
•
If you want the graphic to float, put the figure environment outside of the solution
environment, using to ensure that it’s printed only when solutions
\ifprintanswers
|     | are being | printed, |     | as in |     |     |     |     |
| --- | --------- | -------- | --- | ----- | --- | --- | --- | --- |
\ifprintanswers
\begin{figure}
\includegraphics[width=7cm]{myfigure.pdf}
|     |     | \caption{This |     | is  | a lovely | figure} |     |     |
| --- | --- | ------------- | --- | --- | -------- | ------- | --- | --- |
\label{fig:lovely}
\end{figure}
\fi
• If you don’t want the graphic to float, then omit the figure environment and just put
the \includegraphics command wherever you want the graphic to appear. If you
want the graphic to have a caption, then put the command \usepackage{caption}
|     | in your | preamble |     | and then | use the | \captionof | command, | as in |
| --- | ------- | -------- | --- | -------- | ------- | ---------- | -------- | ----- |
\includegraphics[width=7cm]{myfigure.pdf}
|     | \captionof{figure}{This |     |     |     | is  | a lovely | figure} |     |
| --- | ----------------------- | --- | --- | --- | --- | -------- | ------- | --- |
\label{fig:lovely}
Page 73

| 8.4 Customizing |     | the solution |     |
| --------------- | --- | ------------ | --- |
Thesolutionsprintedbyanyofthesolutionenvironments(seesection8.1)canbecustomized:
• the title (by default, “Solution:”) can be changed (see section 8.4.1),
•
emphasis can be applied to the solution to distinguish it from the surrounding text
| (see section | 8.4.2), and |     |     |
| ------------ | ----------- | --- | --- |
•
advanced users can entirely change the appearance of the solutions by defining a LATEX
| environment | (see section | 8.4.3). |     |
| ----------- | ------------ | ------- | --- |
| 8.4.1 The   | title        |         |     |
The word “Solution:” that you see at the beginning of the solutions printed by the
solution, solutionorbox, solutionorlines, and solutionordottedlines environments
can be changed by redefining the command \solutiontitle. The default value was created
by the command
\newcommand{\solutiontitle}{\noindent\textbf{Solution:}\enspace}
| If, for example, | you give the | command |     |
| ---------------- | ------------ | ------- | --- |
\renewcommand{\solutiontitle}{\noindent\textbf{Solution:}\par\noindent}
| then the solution | environment       | above would | print |
| ----------------- | ----------------- | ----------- | ----- |
| 1. Did you        | mutter something? |             |       |
Solution:
Onceuponamidnightdreary, whileIpondered, weakandweary, Overmanyaquaint
and curious volume of forgotten lore— While I nodded, nearly napping, suddenly
there came a tapping, As of some one gently rapping, rapping at my chamber door.
“’Tis some visitor,” I muttered, “tapping at my chamber door— Only this and
| nothing        | more.”   |     |     |
| -------------- | -------- | --- | --- |
| 8.4.2 Solution | emphasis |     |     |
You can change the appearance of the text of the solution with the \SolutionEmphasis
command. The contents of the solution are enclosed in a group, and that group is begun
with the argument of the most recent \SolutionEmphasis command. The default was
| created by the | command |     |     |
| -------------- | ------- | --- | --- |
\SolutionEmphasis{}
That is, the default is not to add any emphasis at all. If, for example, you give the command
Page 74

\SolutionEmphasis{\itshape\small}
then the solutions will be set in italics, in small type. For another example, if you’ve given
the command \usepackage{color} (or \usepackage{xcolor}) in the preamble of your
document (i.e., after the \documentclass command and before the \begin{document})
and you give the command
\SolutionEmphasis{\color{red}}
then the solutions will be printed in red (assuming your printer is capable of producing that
color).
Note: If you’ve given the command \unframedsolutions (see section 8.2.3), so that
solutions are printed as normal text with no framing or shading, then you’ll almost certainly
want to use the \SolutionEmphasis command to create some visible difference between the
solutions and the surrounding text.
8.4.3 Advanced customizations
The appearance of all of these solution environments can actually be totally customized, if
you’re up to defining a LATEX environment. The appearance of the solution typed into any of
these environments is defined by an environment called TheSolution, and you can change
the definition of TheSolution with a \renewenvironment command. That is, the solution
environment decides whether the command \printanswers has been given and, if so, it
feeds the contents of the solution environment into a TheSolution environment. (The
behavior of a solutionorbox, solutionorlines or solutionordottedlines environment
is similar.) If you use \renewenvironment to change the definition of the TheSolution
environment, you’ll be changing the way the solution is printed. For the default definition
of the TheSolution environment, see the file exam.cls.
8.5 Leaving space for the answers when solutions aren’t printed
Each of the solution, solutionorbox, solutionorlines, solutionordottedlines, and
solutionorgrid environments takes an optional argument:
• In a solution environment this is an amount of blank space to be left (just as if you
had used a \vspace* command (or, if you’ve given the command \unstarredvspace,
as if you had given a \vspace command); see section 7.1) when solutions are not being
printed,
• in a solutionorbox environment this is the height of an empty box to be drawn (just
as if you had used a \makeemptybox command; see section 7.2) when solutions are not
being printed,
• in a solutionorlines environment this is an amount of lined space to be left (just as
if you had used a \fillwithlines command; see section 7.3) when solutions are not
being printed,
Page 75

• in a solutionordottedlines environment this is an amount of dotted lined space to
be left (just as if you had used a \fillwithdottedlines command; see section 7.4)
when solutions are not being printed.
• in a solutionorgrid environment this is an amount of space to be filled with a grid
(just as if you had used a \fillwithgrid command; see section 7.5) when solutions
are not being printed.
For example, if you type
\begin{solution}[2in]
Once upon a midnight dreary, while I pondered, weak and weary, Over
many a quaint and curious volume of forgotten lore--- While I
nodded, nearly napping, suddenly there came a tapping, As of some
one gently rapping, rapping at my chamber door. ‘‘\,’Tis some
visitor,’’ I muttered, ‘‘tapping at my chamber door--- Only this and
nothing more.’’
\end{solution}
then there will be 2 inches of blank space inserted (as if you had given the command
\vspace*{2in}; see section 7.1) when solutions are not being printed, if you type
\begin{solutionorbox}[2in]
Once upon a midnight dreary, while I pondered, weak and weary, Over
many a quaint and curious volume of forgotten lore--- While I
nodded, nearly napping, suddenly there came a tapping, As of some
one gently rapping, rapping at my chamber door. ‘‘\,’Tis some
visitor,’’ I muttered, ‘‘tapping at my chamber door--- Only this and
nothing more.’’
\end{solutionorbox}
then there will be an empty box 2 inches tall inserted (as if you had given the command
\makeemptybox{2in}; see section 7.2) when solutions are not being printed, if you type
\begin{solutionorlines}[2in]
Once upon a midnight dreary, while I pondered, weak and weary, Over
many a quaint and curious volume of forgotten lore--- While I
nodded, nearly napping, suddenly there came a tapping, As of some
one gently rapping, rapping at my chamber door. ‘‘\,’Tis some
visitor,’’ I muttered, ‘‘tapping at my chamber door--- Only this and
nothing more.’’
\end{solutionorlines}
then there will be 2 inches of lined space inserted (as if you had given the command
\fillwithlines{2in}; see section 7.3) when solutions are not being printed, if you type
Page 76

\begin{solutionordottedlines}[2in]
Once upon a midnight dreary, while I pondered, weak and weary, Over
many a quaint and curious volume of forgotten lore--- While I
nodded, nearly napping, suddenly there came a tapping, As of some
one gently rapping, rapping at my chamber door. ‘‘\,’Tis some
visitor,’’ I muttered, ‘‘tapping at my chamber door--- Only this and
nothing more.’’
\end{solutionordottedlines}
then there will be 2 inches of dotted lined space inserted (as if you had given the command
\fillwithdottedlines{2in}; see section 7.4) when solutions are not being printed. and if
you type
\begin{solutionorgrid}[2in]
Once upon a midnight dreary, while I pondered, weak and weary, Over
many a quaint and curious volume of forgotten lore--- While I
nodded, nearly napping, suddenly there came a tapping, As of some
one gently rapping, rapping at my chamber door. ‘‘\,’Tis some
visitor,’’ I muttered, ‘‘tapping at my chamber door--- Only this and
nothing more.’’
\end{solutionordottedlines}
thentherewillbe2inchesofgridinserted(asifyouhadgiventhecommand\fillwithgrid{2in};
see section 7.5) when solutions are not being printed.
8.5.1 Cancelling the space from the optional arguments
If you’ve typed any of the environments solution, solutionorbox, solutionorlines,
solutionordottedlines, or solutionorgrid (see section 8.1), and you’ve
• included an optional argument to leave space for answers when solutions are not being
printed, but
• youwouldnowliketoprinttheexamwithout printingthesolutionsandwithout leaving
space for the answers,
then you can cancel the space that would be created by the optional arguments by using the
cancelspace document class option. That is, if you use the \documentclass command
\documentclass[cancelspace]{exam}
then optional arguments to any of the four solution environments will be ignored. There
are also commands \cancelspace and \nocancelspace; using the document class option
cancelspace is equivalent to giving the command \cancelspace at the beginning of the
file. The command \nocancelspace reverts to the default situation (in which the optional
arguments are not ignored).
The document class option cancelspace has no effect at all if solutions are being printed.
Page 77

Note: The document class option cancelspace and the command \cancelspace only
affecttheoptionalargumentsofofthefivesolutionenvironmentssolution, solutionorbox,
solutionorlines, solutionordottedlines, and solutionorgrid; they do not affect any
\vspace commands that you put into the file.
8.6 The solutionbox environment
The solutionbox environment is different from the other solution environments (solution,
solutionorbox, solutionorlines, solutionordottedlines, and solutionorgrid), in
that
1. The box is always printed, whether answers are being printed or not.
2. The argument giving the size of the box is a required argument, not an optional
argument, and so it should be enclosed in braces, not in brackets. It can be either a
length or \stretch{number}. Note: It is the user’s responsibility to be sure that the
box is large enough to hold the solution! If the solution takes up too much vertical
space, then it will spill out of the bottom of the box, overwriting whatever follows the
box.
3. The solutionbox environment makes no use of the TheSolution environment; the
solutionbox environment is completely freestanding.
If answers are not being printed then only the box is printed, with nothing in it. If answers
are being printed, then the solution is printed inside of the box. (The box printed by the
solutionbox environment can be printed in color; for that, see section 8.7.)
For example, if you type
\begin{solutionbox}{2in}
Once upon a midnight dreary, while I pondered, weak and weary, Over
many a quaint and curious volume of forgotten lore--- While I
nodded, nearly napping, suddenly there came a tapping, As of some
one gently rapping, rapping at my chamber door. ‘‘\,’Tis some
visitor,’’ I muttered, ‘‘tapping at my chamber door--- Only this and
nothing more.’’
\end{solutionbox}
(note that the amount of space is required, and is typed as “{2in}”, rather than “[2in]”)
and solutions are not being printed, then you’ll get
Page 78

If solutions are being printed, then the exact same box would be printed, but it would
| have | the      | solution | printed | inside | of it. |       |     |     |
| ---- | -------- | -------- | ------- | ------ | ------ | ----- | --- | --- |
| 8.7  | Solution |          | box     | frames | in     | color |     |     |
The frames that are printed by the commands that create solution boxes can be printed in
color. (By “frame” we mean the four lines that constitute the box, not any solution that
| may | appear | inside | that    | box.)  | This includes |             |              |       |
| --- | ------ | ------ | ------- | ------ | ------------- | ----------- | ------------ | ----- |
|     | • the  | box    | printed | by the |               | environment | (see section | 8.6), |
solutionbox
• the box printed by the \makeemptybox command (see section 7.2),
• the box printed by the optional argument of the solutionorbox environment (see
|     | section | 8.1), | and |     |     |     |     |     |
| --- | ------- | ----- | --- | --- | --- | --- | --- | --- |
•
|     | the | box | printed | around | the solution | by the |     |     |
| --- | --- | --- | ------- | ------ | ------------ | ------ | --- | --- |
– solution,
– solutionorbox,
– solutionorlines,
|     | –   | solutionordottedlines, |     |     |     | and |     |     |
| --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
– solutionorgrid
environments when solutions are being printed and the default solution appearance
|     | (\framedsolutions) |       |     | is      | being used | (see section | 8.2.1). |     |
| --- | ------------------ | ----- | --- | ------- | ---------- | ------------ | ------- | --- |
|     | If you’ve          | given | the | command |            |              |         |     |
\usepackage{color}
(or\usepackage{xcolor})inthepreambleofyourdocument(i.e.,afterthe\documentclass
command and before the \begin{document} command), then you can give the command
\colorsolutionboxes
Page 79

to have the frame printed in color. The color of the frame will be SolutionBoxColor, the
| default value | of which | was created |     | by the command |     |     |     |
| ------------- | -------- | ----------- | --- | -------------- | --- | --- | --- |
\definecolor{SolutionBoxColor}{gray}{0.8}
You can change the color by giving a new \definecolor command, but you must do this
| after the | \colorsolutionboxes |     | command. |            |           |                  |     |
| --------- | ------------------- | --- | -------- | ---------- | --------- | ---------------- | --- |
| To cancel | color               |     | frames   | and return | to black, | give the command |     |
solutionbox
\nocolorsolutionboxes
| 8.8 Equations |     | inside | solutions |     |     |     |     |
| ------------- | --- | ------ | --------- | --- | --- | --- | --- |
If you use an equation environment inside of a solution, then that environment (like all
equation environments) will be numbered using the equation counter, which will affect the
numbering of equations that follow. However, if you then print a version of your exam with-
out using the \printanswers command (or the documentclass option answers), then the
equation inside the solution environment will not appear, and this will change the equation
| numbers | of the later | equation | environments. |     |     |     |     |
| ------- | ------------ | -------- | ------------- | --- | --- | --- | --- |
If you want to avoid having equation numbers change depending on whether or not
solutions are being printed, you can do this either by using the documentclass option
solutionsreseteqcounter
| or by giving | the | command |     |     |     |     |     |
| ------------ | --- | ------- | --- | --- | --- | --- | --- |
\solutionsreseteqcounter
at the beginning of your file. That command causes equation numbers inside each solution
to be independent of the equation numbers outside of the solution environment or in other
| solution | environments. |     |     |     |     |     |     |
| -------- | ------------- | --- | --- | --- | --- | --- | --- |
In more detail: If you give the command \solutionsreseteqcounter then every time
you begin one of the solution environments, the equation counter will be reset to zero (so
that the first equation environment in the solution will be number 1), and when you end
that solution environment the equation counter will be restored to whatever it was before
| the solution | environment. |     |     |     |     |     |     |
| ------------ | ------------ | --- | --- | --- | --- | --- | --- |
If you’ve given the command \solutionsreseteqcounter and you want to change back
to not having solutions reset the equation counter, you can do that by giving the command
\nosolutionsreseteqcounter
| 8.9 Changes |     | depending |     | on whether | or not | solutions | are being |
| ----------- | --- | --------- | --- | ---------- | ------ | --------- | --------- |
printed
The command \ifprintanswers is provided in case you want to vary what appears on
the exam in ways other than those provided by the solution environments (see section 8),
the \CorrectChoice command in multiple choice environments (see section 5.5), and the
optional argument to the \answerline command (see section 7.7). You use this command
by typing
|     |     |     |     | Page 80 |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- |

\ifprintanswers
| Stuff | to  | appear | only when | answers | are being | printed. |     |
| ----- | --- | ------ | --------- | ------- | --------- | -------- | --- |
\else
| Stuff | to  | appear | only when | answers | are not | being | printed. |
| ----- | --- | ------ | --------- | ------- | ------- | ----- | -------- |
\fi
| The \else | clause | is optional; | you | can | also type |     |     |
| --------- | ------ | ------------ | --- | --- | --------- | --- | --- |
\ifprintanswers
| Stuff | to  | appear | only when | answers | are being | printed. |     |
| ----- | --- | ------ | --------- | ------- | --------- | -------- | --- |
\fi
If you want something printed only when answers are not being printed, you can type
\ifprintanswers
\else
| Stuff | to  | appear | only when | answers | are not | being | printed. |
| ----- | --- | ------ | --------- | ------- | ------- | ----- | -------- |
\fi
Since the exam document class automatically loads the ifthen package, you can accomplish
| the same | things | using | the \ifthenelse |     | command: |     |     |
| -------- | ------ | ----- | --------------- | --- | -------- | --- | --- |
\ifthenelse{\boolean{printanswers}}
| {Stuff | to  | appear | only when | answers | are being | printed.} |           |
| ------ | --- | ------ | --------- | ------- | --------- | --------- | --------- |
| {Stuff | to  | appear | only when | answers | are not   | being     | printed.} |
If you use \ifthenelse, then both cases must be present, even if you leave one of them
empty. Thus, e.g., if you want to print something only when answers are not being printed,
you’d type
\ifthenelse{\boolean{printanswers}}
{}
| {Stuff | to       | appear | only when | answers   | are not | being | printed.} |
| ------ | -------- | ------ | --------- | --------- | ------- | ----- | --------- |
| 8.9.1  | Printing | only   | selected  | solutions |         |       |           |
The \ifprintanswers command can be used to print only certain of the solutions in an
| exam. | To do | that, you’d | put the | lines |     |     |     |
| ----- | ----- | ----------- | ------- | ----- | --- | --- | --- |
\newif\ifprintselected
\printselectedtrue
%\printselectedfalse
\newenvironment{select}
{\ifprintselected
\printanswers
\fi
}
{}
|     |     |     |     |     | Page 81 |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |

intoyourpreamble(i.e.,afterthe\documentclasscommandandbeforethe\begin{document}
command). That defines a select environment, in which you can wrap any of the solution
| environments, |     | as in |     |     |     |     |
| ------------- | --- | ----- | --- | --- | --- | --- |
\begin{select}
\begin{solutionorlines}[1in]
| Only | when | the | number | is  | two. |     |
| ---- | ---- | --- | ------ | --- | ---- | --- |
\end{solutionorlines}
\end{select}
As long as you leave the command \printselectedtrue uncommented, then everything
wrappedinaselectenvironmentwillbeprinted. Ifyoucommentout\printselectedtrue
and uncomment \printselectedfalse, then the select environment will have no effect.
| 9 Grading |          | tables |     | and   | point  | tables |
| --------- | -------- | ------ | --- | ----- | ------ | ------ |
| The exam  | document | class  | can | print | either |        |
•
a grading table, indexed either by question number or by page number, which lists
the points possible and leaves space for you to fill in (by hand) the points earned (see
| section |     | 9.1), or |     |     |     |     |
| ------- | --- | -------- | --- | --- | --- | --- |
•
a point table, indexed either by question number or by page number, which lists the
points possible but does not leave space for you to fill in the points earned (see sec-
| tion | 9.2). |     |     |     |     |     |
| ---- | ----- | --- | --- | --- | --- | --- |
It’s also possible to print either a grading table or point table to cover only part of the exam
| (see section | 9.4). |     |     |     |     |     |
| ------------ | ----- | --- | --- | --- | --- | --- |
If the exam has any bonus points (see section 4.6), then the bonus points will be ignored
by the tables described in sections 9.1, 9.2, and 9.4, but it’s possible to print bonus grading
tables and bonus point tables that list the bonus points and ignore the non-bonus points
(see section 9.7) or combined grading tables and combined point tables that list both regular
| points | and bonus | points | (see | section | 9.8). |     |
| ------ | --------- | ------ | ---- | ------- | ----- | --- |
9.1 Grading tables indexed by question number or by page num-
ber
The document class can print a grading table, indexed either by question number or
exam
| by page | number. | That | is, you | can | print |     |
| ------- | ------- | ---- | ------- | --- | ----- | --- |
• a table listing the question numbers (or question titles for questions created using the
\titledquestion command instead of the \question command; see section 4.5) and
the total points possible for each question (including all of its parts, subparts, and
subsubparts) and leaving space for you to fill in (by hand) the points earned on each
| question, |     | or  |     |     |      |     |
| --------- | --- | --- | --- | --- | ---- | --- |
|           |     |     |     |     | Page | 82  |

•
a table listing each page that has at least one question, part, subpart, or subsubpart
with points assigned to it, the total number of points possible on that page, and leaving
|     | space | for | you to | fill in (by | hand) | the points | earned | on that page. |
| --- | ----- | --- | ------ | ----------- | ----- | ---------- | ------ | ------------- |
In order to use this feature you must either include the optional argument addpoints in
your \documentclass command (as in \documentclass[addpoints]{exam}) or give the
command \addpoints (see section 3.1), and there must be only one questions environment
in the entire exam. In addition, you must run LATEX twice after making any changes to
the file in order to make sure that the point values are correct on a grading table indexed
by question number and at least three times for a grading table indexed by page number.
(Since the table appears on the third run of LATEX, and the space it occupies can change the
page on which each question falls, it may take a fourth run of LATEX for the table to have
| the | points      | per | page correct.) |     |         |          |     |     |
| --- | ----------- | --- | -------------- | --- | ------- | -------- | --- | --- |
|     | The command |     | to create      | a   | grading | table is |     |     |
\gradetable
| and | it takes | two | optional | arguments: |     |     |     |     |
| --- | -------- | --- | -------- | ---------- | --- | --- | --- | --- |
1. The first optional argument can be either [v] or [h], to choose between a vertically
|     | oriented | table | and | a horizontally |     | oriented | table, | and |
| --- | -------- | ----- | --- | -------------- | --- | -------- | ------ | --- |
2. the second optional argument can be either [questions] or [pages], to choose be-
tween a table indexed by question number and a table indexed by page number.
That is,
•
\gradetable[v][questions] prints a vertically oriented table indexed by question
number,
• \gradetable[h][questions] prints a horizontally oriented table indexed by question
number,
• \gradetable[v][pages] prints a vertically oriented table indexed by page number,
and
•
\gradetable[h][pages] prints a horizontally oriented table indexed by page number.
If you leave out the optional arguments (i.e., if you give the command as “\gradetable”)
| you’ll | get | a vertically |     | oriented | table | indexed | by question | number. |
| ------ | --- | ------------ | --- | -------- | ----- | ------- | ----------- | ------- |
For example, if the exam has 8 questions, each worth a total of 15 points, and you type
\begin{center}
\gradetable[v][questions]
\end{center}
| then | you’ll | get |     |     |     |      |     |     |
| ---- | ------ | --- | --- | --- | --- | ---- | --- | --- |
|      |        |     |     |     |     | Page | 83  |     |

|        |          |     | Question Points | Score |     |     |
| ------ | -------- | --- | --------------- | ----- | --- | --- |
|        |          |     | 1               | 15    |     |     |
|        |          |     | 2               | 15    |     |     |
|        |          |     | 3               | 15    |     |     |
|        |          |     | 4               | 15    |     |     |
|        |          |     | 5               | 15    |     |     |
|        |          |     | 6               | 15    |     |     |
|        |          |     | 7               | 15    |     |     |
|        |          |     | 8               | 15    |     |     |
|        |          |     | Total: 120      |       |     |     |
| and if | you type |     |                 |       |     |     |
\begin{center}
\gradetable[h][questions]
\end{center}
| then you’ll | get       |       |       |       |       |       |
| ----------- | --------- | ----- | ----- | ----- | ----- | ----- |
|             | Question: | 1 2   | 3 4   | 5 6   | 7 8   | Total |
|             | Points:   | 15 15 | 15 15 | 15 15 | 15 15 | 120   |
Score:
The number of points listed for a question is the sum of the point values for that question
| and all | of its parts, | subparts, and | subsubparts. |     |     |     |
| ------- | ------------- | ------------- | ------------ | --- | --- | --- |
If those 8 questions are distributed two to a page on each of pages 2 through 5 and if you
type
\begin{center}
\gradetable[v][pages]
\end{center}
| then you’ll | get |     |             |       |     |     |
| ----------- | --- | --- | ----------- | ----- | --- | --- |
|             |     |     | Page Points | Score |     |     |
|             |     |     | 2 30        |       |     |     |
|             |     |     | 3 30        |       |     |     |
|             |     |     | 4 30        |       |     |     |
|             |     |     | 5 30        |       |     |     |
|             |     |     | Total: 120  |       |     |     |
|             |     |     | Page        | 84    |     |     |

| and if you | type |     |     |     |     |     |
| ---------- | ---- | --- | --- | --- | --- | --- |
\begin{center}
\gradetable[h][pages]
\end{center}
| then you’ll | get |         |     |     |       |       |
| ----------- | --- | ------- | --- | --- | ----- | ----- |
|             |     | Page:   | 2   | 3   | 4 5   | Total |
|             |     | Points: | 30  | 30  | 30 30 | 120   |
Score:
Warning: If you have a large number of questions on the exam, then these tables can
easily become too large to fit on the page. If this becomes a problem, then you can either
•
create grading ranges (see section 9.4) and print several partial grading tables, making
| each | one small | enough | to fit on the | page, | or  |     |
| ---- | --------- | ------ | ------------- | ----- | --- | --- |
•
usethe\multirowgradetableor\multicolumngradetablecommand(seesection9.1.1
and section 9.1.2) to create a grading table with multiple rows or multiple columns.
| 9.1.1 Grading |     | tables with | multiple | rows |     |     |
| ------------- | --- | ----------- | -------- | ---- | --- | --- |
If you want to print a horizontal grading table but the table would be too large for the page,
you can print a grading table with multiple rows by giving the command
|     | \multirowgradetable{numrows}[questions |     |     |     |     | or pages] |
| --- | -------------------------------------- | --- | --- | --- | --- | --------- |
Note that the first argument (numrows) is required, and so it is enclosed in braces, but the
second argument (questions or pages) is optional, and is enclosed in square brackets, just
as in the command (see section 9.1). For example, to print a grading table
\gradetable
| with 3 rows | indexed | by questions, | you | would | give the command |     |
| ----------- | ------- | ------------- | --- | ----- | ---------------- | --- |
\multirowgradetable{3}[questions]
The command
\gradetable[h][questions]
| is equivalent | to  |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | --- | --- |
\multirowgradetable{1}[questions]
The distance between the rows of a multirow table is \doublerulesep, the default value
of which is 2.0pt. You can change that using a \setlength command, as in
\setlength{\doublerulesep}{0.5in}
Page 85

| (see section 9.10). |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- |
For example, if an exam has 16 questions, each worth a total of 15 points, and you type
\begin{center}
\setlength{\doublerulesep}{0.25in}
\multirowgradetable{2}[questions]
\end{center}
| then you’ll get |     |       |          |       |     |
| --------------- | --- | ----- | -------- | ----- | --- |
| Question:       | 1   | 2 3   | 4 5 6    | 7 8   | 9   |
| Points:         | 15  | 15 15 | 15 15 15 | 15 15 | 15  |
Score:
| Question: | 10  | 11 12 | 13 14 15 | 16  | Total |
| --------- | --- | ----- | -------- | --- | ----- |
| Points:   | 15  | 15 15 | 15 15 15 | 15  | 240   |
Score:
| 9.1.2 Grading | tables with | multiple | columns |     |     |
| ------------- | ----------- | -------- | ------- | --- | --- |
If you want to print a vertical grading table but the table would be too large for the page,
you can print a grading table with multiple columns by giving the command
|     | \multicolumngradetable{numcols}[questions |     |     | or pages] |     |
| --- | ----------------------------------------- | --- | --- | --------- | --- |
Note that the first argument (numcols) is required, and so it is enclosed in braces, but the
second argument (questions or pages) is optional, and is enclosed in square brackets, just
as in the \gradetable command (see section 9.1). For example, to print a grading table
with 3 columns indexed by questions, you would give the command
\multicolumngradetable{3}[questions]
The command
\gradetable[v][questions]
| is equivalent to |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- |
\multicolumngradetable{1}[questions]
Thedistancebetweenthecolumnsofamulticolumntableis\doublerulesep, thedefault
value of which is 2.0pt. You can change that using a \setlength command, as in
\setlength{\doublerulesep}{0.5in}
Page 86

| (see | section | 9.10). |     |     |     |     |     |
| ---- | ------- | ------ | --- | --- | --- | --- | --- |
For example, if an exam has 10 questions, each worth a total of 15 points, and you type
\begin{center}
\setlength{\doublerulesep}{0.5in}
\multicolumngradetable{2}[questions]
\end{center}
| then | you’ll | get |          |              |     |          |              |
| ---- | ------ | --- | -------- | ------------ | --- | -------- | ------------ |
|      |        |     | Question | Points Score |     | Question | Points Score |
|      |        |     | 1        | 15           |     | 7        | 15           |
|      |        |     | 2        | 15           |     | 8        | 15           |
|      |        |     | 3        | 15           |     | 9        | 15           |
|      |        |     | 4        | 15           |     | 10       | 15           |
|      |        |     | 5        | 15           |     |          |              |
|      |        |     | 6        | 15           |     | Total:   | 150          |
9.2 Point tables indexed by question number or by page number
Point tables are similar to grading tables (see section 9.1), except that there is no place in
| the | table       | to fill | in the    | points earned. |          |     |     |
| --- | ----------- | ------- | --------- | -------------- | -------- | --- | --- |
|     | The command |         | to create | a point        | table is |     |     |
\pointtable
| and | it takes | two | optional | arguments: |     |     |     |
| --- | -------- | --- | -------- | ---------- | --- | --- | --- |
1. The first optional argument can be either [v] or [h], to choose between a vertically
|     | oriented | table | and | a horizontally | oriented | table, and |     |
| --- | -------- | ----- | --- | -------------- | -------- | ---------- | --- |
2. the second optional argument can be either [questions] or [pages], to choose be-
tween a table indexed by question number and a table indexed by page number.
That is,
• \pointtable[v][questions] prints a vertically oriented table indexed by question
number,
•
\pointtable[h][questions] prints a horizontally oriented table indexed by question
number,
•
\pointtable[v][pages] prints a vertically oriented table indexed by page number,
and
|     |     |     |     |     | Page 87 |     |     |
| --- | --- | --- | --- | --- | ------- | --- | --- |

•
\pointtable[h][pages] prints a horizontally oriented table indexed by page number.
If you leave out the optional arguments (i.e., if you give the command as “\pointtable”)
| you’ll | get a vertically | oriented table | indexed | by question | number. |     |
| ------ | ---------------- | -------------- | ------- | ----------- | ------- | --- |
For example, if the exam has 8 questions, each worth a total of 15 points, and you type
\begin{center}
\pointtable[v][questions]
\end{center}
| then you’ll | get      |     |          |        |     |     |
| ----------- | -------- | --- | -------- | ------ | --- | --- |
|             |          |     | Question | Points |     |     |
|             |          |     | 1        | 15     |     |     |
|             |          |     | 2        | 15     |     |     |
|             |          |     | 3        | 15     |     |     |
|             |          |     | 4        | 15     |     |     |
|             |          |     | 5        | 15     |     |     |
|             |          |     | 6        | 15     |     |     |
|             |          |     | 7        | 15     |     |     |
|             |          |     | 8        | 15     |     |     |
|             |          |     | Total:   | 120    |     |     |
| and if      | you type |     |          |        |     |     |
\begin{center}
\pointtable[h][questions]
\end{center}
| then you’ll | get |             |       |          |       |       |
| ----------- | --- | ----------- | ----- | -------- | ----- | ----- |
|             |     | Question: 1 | 2 3   | 4 5 6    | 7 8   | Total |
|             |     | Points: 15  | 15 15 | 15 15 15 | 15 15 | 120   |
The number of points listed for a question is the sum of the point values for that question
| and all | of its parts, | subparts, and | subsubparts. |     |     |     |
| ------- | ------------- | ------------- | ------------ | --- | --- | --- |
If those 8 questions are distributed two to a page on each of pages 2 through 5 and if you
type
\begin{center}
\pointtable[v][pages]
\end{center}
|     |     |     | Page | 88  |     |     |
| --- | --- | --- | ---- | --- | --- | --- |

| then you’ll | get |     |     |     |
| ----------- | --- | --- | --- | --- |
Page Points
|                 |     |     | 2 30       |     |
| --------------- | --- | --- | ---------- | --- |
|                 |     |     | 3 30       |     |
|                 |     |     | 4 30       |     |
|                 |     |     | 5 30       |     |
|                 |     |     | Total: 120 |     |
| and if you type |     |     |            |     |
\begin{center}
\pointtable[h][pages]
\end{center}
| then you’ll | get |         |          |         |
| ----------- | --- | ------- | -------- | ------- |
|             |     | Page:   | 2 3 4    | 5 Total |
|             |     | Points: | 30 30 30 | 30 120  |
Warning: If you have a large number of questions on the exam, then these tables can
easily become too large to fit on the page. If this becomes a problem, then you can either
•
create grading ranges (see section 9.4) and print several partial point tables, making
| each one | small enough | to fit on | the page, or |     |
| -------- | ------------ | --------- | ------------ | --- |
• usethe\multirowpointtableor\multicolumnpointtablecommand(seesection9.2.1
and section 9.2.2) to create a point table with multiple rows or multiple columns.
| 9.2.1 Point | tables with | multiple | rows |     |
| ----------- | ----------- | -------- | ---- | --- |
If you want to print a horizontal point table but the table would be too large for the page,
you can print a point table with multiple rows by giving the command
\multirowpointtable{numrows}[questions or pages]
Note that the first argument (numrows) is required, and so it is enclosed in braces, but the
second argument (questions or pages) is optional, and is enclosed in square brackets, just
as in the \pointtable command (see section 9.2). For example, to print a point table with
| 3 rows indexed | by questions, | you would | give the | command |
| -------------- | ------------- | --------- | -------- | ------- |
\multirowpointtable{3}[questions]
The command
|     |     |     | Page 89 |     |
| --- | --- | --- | ------- | --- |

\pointtable[h][questions]
| is equivalent | to  |     |     |     |
| ------------- | --- | --- | --- | --- |
\multirowpointtable{1}[questions]
The distance between the rows of a multirow table is \doublerulesep, the default value
of which is 2.0pt. You can change that using a \setlength command, as in
\setlength{\doublerulesep}{0.5in}
| (see section | 9.10).       |               |         |     |
| ------------ | ------------ | ------------- | ------- | --- |
| 9.2.2        | Point tables | with multiple | columns |     |
If you want to print a vertical point table but the table would be too large for the page, you
can print a point table with multiple columns by giving the command
\multicolumnpointtable{numcols}[questions or pages]
Note that the first argument (numcols) is required, and so it is enclosed in braces, but the
second argument (questions or pages) is optional, and is enclosed in square brackets, just
as in the \pointtable command (see section 9.2). For example, to print a point table with
| 3 columns | indexed | by questions, | you would | give the command |
| --------- | ------- | ------------- | --------- | ---------------- |
\multicolumnpointtable{3}[questions]
The command
\pointtable[v][questions]
| is equivalent | to  |     |     |     |
| ------------- | --- | --- | --- | --- |
\multicolumnpointtable{1}[questions]
Thedistancebetweenthecolumnsofamulticolumntableis\doublerulesep, thedefault
value of which is 2.0pt. You can change that using a \setlength command, as in
\setlength{\doublerulesep}{0.5in}
| (see section | 9.10). |     |     |     |
| ------------ | ------ | --- | --- | --- |
Page 90

| 9.3        | Table entries | as clickable |     | links |
| ---------- | ------------- | ------------ | --- | ----- |
| If you put | the command   |              |     |       |
\usepackage{hyperref}
intothepreambleofyourdocument(i.e., afterthe\documentclasscommandandbeforethe
\begin{document} command) and then produce a pdf file (either using dvipdf or directly
| by using | pdflatex), then |     |     |     |
| -------- | --------------- | --- | --- | --- |
•
in a grading table or point table indexed by question number the question numbers in
the table will be clickable links that take you to the corresponding question, and
• in a grading table or point table indexed by page number the page numbers in the
table will be clickable links that take you to the corresponding page.
If you create questions using the \titledquestion command instead of the \question
command (see section 4.5), then a grading table or point table indexed by question number
will show the titles of those questions instead of the numbers of those questions, and those
question titles will be clickable links that take you to the corresponding question.
9.4 Grading ranges, partial grading tables, and partial point ta-
bles
It is possible to define one or more “grading ranges”, and then to count the points in a range
and create grading tables and point tables that cover only that range.
In more detail: You can define a grading range by choosing a name with which to label
| the range, | e.g., “myrange”, | and then | putting | the command |
| ---------- | ---------------- | -------- | ------- | ----------- |
\begingradingrange{myrange} at the start of the range and the command
| \endgradingrange{myrange} |                       |     | at the | end of the range. |
| ------------------------- | --------------------- | --- | ------ | ----------------- |
| You can                   | then use the commands |     |        |                   |
• \pointsinrange{myrange}, which will expand to the number of points in the range,
•
\firstqinrange{myrange}, which will expand to the number of the first question in
| the | range, |     |     |     |
| --- | ------ | --- | --- | --- |
•
\lastqinrange{myrange}, which will expand to the number of the last question in
| the | range, and |     |     |     |
| --- | ---------- | --- | --- | --- |
• \numqinrange{myrange}, which will expand to the number of questions in the range.
You can define as many grading ranges as you like, wherever you like. That is, grading
ranges do not need to be nested; you can begin the range otherrange somewhere in the
middle of the range myrange and then end the range otherrange after the end of myrange.
|     |     |     |     | Page 91 |
| --- | --- | --- | --- | ------- |

You can create a grading table or point table that covers only the questions in a range
by using the \partialgradetable or \partialpointtable command. These are similar
to the \gradetable and \pointtable commands, except that they each have one required
argument (the name of the grading range) before the two optional arguments (the first of
which must be either [v] or [h] and the second of which must be either [questions] or
[pages]). For example, the command
\partialgradetable{myrange}[v][questions]
would create a vertically grading oriented table indexed by the questions in the range, and
the command
\partialgradetable{myrange}[v][pages]
would create a vertically oriented grading table indexed by all pages with points starting
with the page containing the command \begingradingrange{myrange} and ending with
the page containing the command \endgradingrange{myrange}
Iftheexamhasanybonuspoints(seesection4.6),thenthebonuspointswillbeignoredby
the\pointsinrange, \partialgradetable, and\partialpointtablecommands, but they
will be counted by the \bonuspointsinrange command (see section 9.7) and tabulated by
the\partialbonusgradetable,\partialbonuspointtable,\partialcombinedgradetable,
and \partialcombinedponttable commands (see section 9.7 and section 9.8).
9.4.1 Partial grading tables and partial point tables with multiple rows
If you want to print a horizontal partial grading table or partial point table but the table
would be too large for the page, you can print a partial grading table or partial point table
with multiple rows by giving the one of the commands
\multirowpartialgradetable{numrows}{rangename}[questions or pages]
\multirowpartialpointtable{numrows}{rangename}[questions or pages]
Note that the first two arguments (numrows and rangename) are required, and so they are
enclosed in braces, but the third argument (questions or pages) is optional, and is enclosed
insquarebrackets, justasinthe\partialgradetableand\partialpointtablecommands
(see section 9.4). For example, to print a partial grading table with 3 rows covering the range
myrange indexed by questions, you would give the command
\multirowpartialgradetable{3}{myrange}[questions]
The command
\partialgradetable{myrange}[h][questions]
is equivalent to
\multirowpartialgradetable{1}{myrange}[questions]
The distance between the rows of a multirow table is \doublerulesep, the default value
of which is 2.0pt. You can change that using a \setlength command, as in
\setlength{\doublerulesep}{0.5in}
(see section 9.10).
Page 92

9.4.2 Partial grading tables and partial point tables with multiple columns
If you want to print a vertical partial grading table or partial point table but the table would
be too large for the page, you can print a partial grading table or partial point table with
multiple columns by giving one of the commands
\multicolumnpartialgradetable{numcols}{rangename}[questions or pages]
\multicolumnpartialpointtable{numcols}{rangename}[questions or pages]
Note that the first two arguments (numcols and rangename) are required, and so they are
enclosed in braces, but the third argument (questions or pages) is optional, and is enclosed
insquarebrackets, justasinthe\partialgradetableand\partialpointtablecommands
(see section 9.4). For example, to print a partial grading table with 3 columns covering the
range myrange indexed by questions, you would give the command
\multicolumnpartialgradetable{3}{myrange}[questions]
The command
\partialgradetable{myrange}[v][questions]
is equivalent to
\multicolumnpartialgradetable{1}{myrange}[questions]
Thedistancebetweenthecolumnsofamulticolumntableis\doublerulesep, thedefault
value of which is 2.0pt. You can change that using a \setlength command, as in
\setlength{\doublerulesep}{0.5in}
(see section 9.10).
9.5 \pointsofquestion
Ifyouusethedocumentclassoptionaddpoints(asin\documentclass[addpoints]{exam})
or give the command \addpoints (see section 3.1), then you can use the
\pointsofquestion
command. This command takes one argument, which must be the number of a question on
the exam, and it prints the total number of points for that question. That is:
• \pointsofquestion{1} prints the sum of the point values for question 1 and all of its
parts, subparts, and subsubparts.
• \pointsofquestion{2} prints the sum of the point values for question 2 and all of its
parts, subparts, and subsubparts.
• Etc.
Page 93

The\pointsofquestioncommandisusedbythe\gradetableand\pointtablecommands
(see section 9), and it can be used to create a table using LATEX’s tabular environment when
the tables produced using the \gradetable and \pointtable commands either don’t fit on
thepageorareunsuitableforsomeotherreason. Itcanalsobeusedina\qformatcommand
to list the total number of points of all parts, subparts, and subsubparts of a question on
the line with the question number (see section 4.4.1).
The \pointsofquestion command ignores any bonus points that you may have cre-
ated (see section 4.6). The \bonuspointsofquestion command, however, counts the bonus
points (see section 9.7).
9.6 \pointsonpage
Ifyouusethedocumentclassoptionaddpoints(asin\documentclass[addpoints]{exam})
or give the command \addpoints (see section 3.1), then you can use the \pointsonpage
command. This command takes one argument, which must be the number of a page of the
exam, and it prints the total number of points for all the questions, parts, subparts, and
subsubparts on that page. That is:
• \pointsonpage{1} prints the sum of the point values for all questions, etc., on page
1,
• \pointsonpage{2} prints the sum of the point values for all questions, etc., on page
2,
• Etc.
This command can be used to create a table using LATEX’s tabular environment when the
tables produced using the \gradetable and \pointtable commands either don’t fit on the
page or are unsuitable for some other reason. It can also be used in headers and footers
to print on each page the total number of points available on that page; for example, the
command
\runningfooter{}
{}
{Points earned: \makebox[1in]{\hrulefill}
out of a possible \pointsonpage{\thepage} points}
(see section 11.3.1) will produce the footer
Points earned: out of a possible 20 points
on all pages after the first. (For another example, see section 11.10.7)
Caution: The command \pointsonpage{\thepage} will work reliably only in headers
and footers, since the command \thepage will work reliably only in headers and footers.
The \pointsonpage command ignores any bonus points that you may have created (see
section 4.6). The \bonuspointsonpage command, however, counts the bonus points (see
section 9.7).
Page 94

| 9.7 Bonus | grading | tables | and bonus | point tables |     |
| --------- | ------- | ------ | --------- | ------------ | --- |
If your exam contains any bonus points (see section 4.6), then those bonus points will
be ignored by the grading table and point table commands described in sections 9.1, 9.2,
and9.4andbythe\pointsofquestion(seesection9.5)and\pointsonpage(seesection9.6)
commands. There are, however, analogous commands that count only the bonus points and
ignore the non-bonus points. (There are also commands that create tables listing both non-
bonus and bonus points; see section 9.8.) These commands, and the non-bonus commands
| to which they                   | correspond, | are as follows: |     |                            |        |
| ------------------------------- | ----------- | --------------- | --- | -------------------------- | ------ |
| Bonus points                    |             |                 |     | Non-bonus                  | points |
| \bonusgradetable                |             |                 |     | \gradetable                |        |
| \multirowbonusgradetable        |             |                 |     | \multirowgradetable        |        |
| \multicolumnbonusgradetable     |             |                 |     | \multicolumngradetable     |        |
| \bonuspointtable                |             |                 |     | \pointtable                |        |
| \multirowbonuspointtable        |             |                 |     | \multirowpointtable        |        |
| \multicolumnbonuspointtable     |             |                 |     | \multicolumnpointtable     |        |
| \partialbonusgradetable         |             |                 |     | \partialgradetable         |        |
| \multirowpartialbonusgradetable |             |                 |     | \multirowpartialgradetable |        |
\multicolumnpartialbonusgradetable \multicolumnpartialgradetable
| \partialbonuspointtable         |     |     |     | \partialpointtable         |     |
| ------------------------------- | --- | --- | --- | -------------------------- | --- |
| \multirowpartialbonuspointtable |     |     |     | \multirowpartialpointtable |     |
\multicolumnpartialbonuspointtable \multicolumnpartialpointtable
| \bonuspointsinrange    |     |     |     | \pointsinrange    |     |
| ---------------------- | --- | --- | --- | ----------------- | --- |
| \bonuspointsofquestion |     |     |     | \pointsofquestion |     |
| \bonuspointsonpage     |     |     |     | \pointsonpage     |     |
All of the the commands in the first column count bonus points and ignore non-bonus points,
while all of the commands in the second column count non-bonus points and ignore bonus
| points. The | commands |     |     |     |     |
| ----------- | -------- | --- | --- | --- | --- |
\partialbonusgradetable,
\multirowpartialbonusgradetable,
\multicolumnpartialbonusgradetable,
\partialbonuspointtable,
|     |     | \multirowpartialbonuspointtable, |     |     | and |
| --- | --- | -------------------------------- | --- | --- | --- |
\multicolumnpartialbonuspointtable
use the same \begingradingrange and \endgradingrange commands that are used by the
corresponding non-bonus versions (see section 9.4). Just as is described in section 9.3 for
| their non-bonus | counterparts, | if you put | the command |     |     |
| --------------- | ------------- | ---------- | ----------- | --- | --- |
\usepackage{hyperref}
Page 95

intothepreambleofyourdocument(i.e., afterthe\documentclasscommandandbeforethe
\begin{document} command) and then produce a pdf file (either using dvipdf or directly
| by using | pdflatex), |     | then |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
•
inabonusgradingtableorbonuspointtableindexedbyquestionnumber, thequestion
numbers (or question titles, if you used \bonustitledquestion; see section 4.6) in the
table will be clickable links that take you to the corresponding question, and
• inabonusgradingtableorbonuspointtableindexedbypagenumberthepagenumbers
in the table will be clickable links that take you to the corresponding page.
For example, if the exam has 8 questions, with each odd numbered question worth a total
of 10 regular points and each even numbered question worth a total of 5 bonus points, and
you type
\begin{center}
\bonusgradetable[h][questions]
\end{center}
| then | you’ll get |         |     |     |     |     |     |     |       |       |
| ---- | ---------- | ------- | --- | --- | --- | --- | --- | --- | ----- | ----- |
|      | Question:  |         |     | 1   | 2   | 3   | 4   | 5   | 6 7 8 | Total |
|      | Bonus      | Points: |     | 0   | 5   | 0   | 5   | 0   | 5 0 5 | 20    |
Score:
| 9.8 | Combined |     | grading |     | tables | and | combined |     | point tables |     |
| --- | -------- | --- | ------- | --- | ------ | --- | -------- | --- | ------------ | --- |
There are commands for producing combined grading and point tables, both partial and
full, that tabulate both regular points and bonus points (see section 4.6). The single-row
and single-column versions of these commands, and the non-bonus and bonus commands to
| which | they        | correspond, |      | are              |       |        |      |                     |          |     |
| ----- | ----------- | ----------- | ---- | ---------------- | ----- | ------ | ---- | ------------------- | -------- | --- |
|       | Non-Bonus   | points      | only |                  | Bonus | points | only |                     | Combined |     |
|       | \gradetable |             |      | \bonusgradetable |       |        |      | \combinedgradetable |          |     |
|       | \pointtable |             |      | \bonuspointtable |       |        |      | \combinedpointtable |          |     |
\partialgradetable \partialbonusgradetable \partialcombinedgradetable
\partialpointtable \partialbonuspointtable \partialcombinedpointtable
The first two commands in each column take two optional arguments, the first being either
[v] or [h] and the second being either [questions] or [pages]. The last two commands
in each column take one required argument, the name of the grading range (defined using
the \begingradingrange and \endgradingrange commands; see section 9.4), and then the
same two optional arguments as the other commands (the first being either [v] or [h] and
| the | second being |     | either | [questions] |     | or [pages]). |     |     |     |     |
| --- | ------------ | --- | ------ | ----------- | --- | ------------ | --- | --- | --- | --- |
The multirow and multicolumn versions of combined grading tables and combined point
| tables | are produced |     | by the | commands |     |      |     |     |     |     |
| ------ | ------------ | --- | ------ | -------- | --- | ---- | --- | --- | --- | --- |
|        |              |     |        |          |     | Page | 96  |     |     |     |

| \multirowcombinedgradetable{numrows}[questions |     |     |     | or pages] |     |     |
| ---------------------------------------------- | --- | --- | --- | --------- | --- | --- |
| \multirowcombinedpointtable{numrows}[questions |     |     |     | or pages] |     |     |
\multirowpartialcombinedgradetable{numrows}{rangename}[questions or pages]
\multirowpartialcombinedpointtable{numrows}{rangename}[questions or pages]
| \multicolumncombinedgradetable{numcols}[questions |     |     |     | or  | pages] |     |
| ------------------------------------------------- | --- | --- | --- | --- | ------ | --- |
| \multicolumncombinedpointtable{numcols}[questions |     |     |     | or  | pages] |     |
\multicolumnpartialcombinedgradetable{numcols}{rangename}[questions or pages]
\multicolumnpartialcombinedpointtable{numcols}{rangename}[questions or pages]
Thedistancebetweentherowsofamultirowtableandbetweenthecolumnsofamulticolumn
table is \doublerulesep, the default value of which is 2.0pt. You can change that using a
| \setlength | command, | as in |     |     |     |     |
| ---------- | -------- | ----- | --- | --- | --- | --- |
\setlength{\doublerulesep}{0.5in}
| (see section | 9.10). |     |     |     |     |     |
| ------------ | ------ | --- | --- | --- | --- | --- |
Just as is described in section 9.3 for their regular points and section 9.7 for bonus points,
| if you put | the command |     |     |     |     |     |
| ---------- | ----------- | --- | --- | --- | --- | --- |
\usepackage{hyperref}
intothepreambleofyourdocument(i.e., afterthe\documentclasscommandandbeforethe
\begin{document} command) and then produce a pdf file (either using dvipdf or directly
| by using | pdflatex), then |     |     |     |     |     |
| -------- | --------------- | --- | --- | --- | --- | --- |
•
in a combined grading table or combined point table indexed by question number,
the question numbers (or question titles, if you used either \titledquestion (see
section 4.5) or (see section 4.6)) in the table will be clickable
\bonustitledquestion
| links | that take | you to the corresponding |     | question, and |     |     |
| ----- | --------- | ------------------------ | --- | ------------- | --- | --- |
• in a combined grading table or combined point table indexed by page number the page
numbers in the table will be clickable links that take you to the corresponding page.
For example, if the exam has 8 questions, with each odd numbered question worth a total
of 10 regular points and each even numbered question worth a total of 5 bonus points, and
you type
\begin{center}
\combinedgradetable[h][questions]
\end{center}
| then you’ll | get     |      |     |        |      |       |
| ----------- | ------- | ---- | --- | ------ | ---- | ----- |
| Question:   |         | 1 2  | 3   | 4 5 6  | 7 8  | Total |
| Points:     |         | 10 0 | 10  | 0 10 0 | 10 0 | 40    |
| Bonus       | Points: | 0 5  | 0   | 5 0 5  | 0 5  | 20    |
Score:
|     |     |     | Page | 97  |     |     |
| --- | --- | --- | ---- | --- | --- | --- |

9.9 Changing the total points in a table
There are commands for changing the total points and total bonus points in grading and
point tables, so that the stated point total will not equal the sum of the point values in the
table. These commands are intended for exams in which the students are required to do
some subset of the problems, but not all of them, and so the total number of points possible
on the exam is less than the sum of the points for all of the questions. The commands are
\settabletotalpoints
\settabletotalbonuspoints
Each of those commands takes one argument. After giving the command
\settabletotalpoints{number}
any grading or point table (regular or combined, partial or full) will list the total points as
number instead of the actual total number of points in the table. After giving the command
\settabletotalbonuspoints{number}
any grading or point table (bonus or combined, partial or full) will list the total bonus points
as number instead of the actual total number of bonus points in the table.
To have these commands affect only a single table, confine the command and the com-
mand to create the table inside of a group (possibly by just placing those commands inside
of a center environment). For example, if an exam has 8 questions, each worth 10 points,
and the students are required to do any 6 of the 8, then the commands
\begin{center}
\settabletotalpoints{60}
\gradetable[h][questions]
\end{center}
will produce
Question: 1 2 3 4 5 6 7 8 Total
Points: 10 10 10 10 10 10 10 10 60
Score:
and no other tables will be affected by that \settabletotalpoints command.
9.10 Customizing the tables
There are four ways in which you can customize the appearance of grading tables and point
tables:
• You can change the words (and the fonts) that appear in the table.
Page 98

•
You can change the minimum width of the blank cells into which you will write the
scores.
•
You can change the value of \baselinestretch used for the table.
•
You can change the distance between the rows in a multirow table and the distance
|     | between            | the | columns   | in a multicolumn |     | table. |          |         |       |        |       |       |
| --- | ------------------ | --- | --------- | ---------------- | --- | ------ | -------- | ------- | ----- | ------ | ----- | ----- |
| For | all grading        |     | and point | tables:          |     |        |          |         |       |        |       |       |
|     | \cellwidth{length} |     |           |                  |     |        | sets the | minimum | width | of the | blank | cells |
to length
\gradetablestretch{number} uses number as the \baselinestretch
\setlength{\doublerulesep}{length} sets the distance between the columns of
|     |     |     |     |     |     |     | a multicolumn |      | table and | the      | distance | be- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ---- | --------- | -------- | -------- | --- |
|     |     |     |     |     |     |     | tween the     | rows | of a      | multirow | table    | to  |
length.
| For | vertical   | non-bonus |                 | tables: |             |      |        |                 |         |     |     |     |
| --- | ---------- | --------- | --------------- | ------- | ----------- | ---- | ------ | --------------- | ------- | --- | --- | --- |
|     |            |           | Command         |         |             |      | Effect |                 |         |     |     |     |
|     |            |           | \vqword{text}   |         | substitutes |      | text   | for “Question”  |         |     |     |     |
|     |            |           | \vpgword{text}  |         | substitutes |      | text   | for “Page”      |         |     |     |     |
|     |            |           |                 |         | substitutes |      |        | for “Points”    |         |     |     |     |
|     |            |           | \vpword{text}   |         |             |      | text   |                 |         |     |     |     |
|     |            |           | \vsword{text}   |         | substitutes |      | text   | for “Score”     |         |     |     |     |
|     |            |           | \vtword{text}   |         | substitutes |      | text   | for “Total:”    |         |     |     |     |
| For | horizontal |           | non-bonus       | tables: |             |      |        |                 |         |     |     |     |
|     |            |           | Command         |         |             |      | Effect |                 |         |     |     |     |
|     |            |           | \hqword{text}   |         | substitutes |      | text   | for “Question:” |         |     |     |     |
|     |            |           | \hpgword{text}  |         | substitutes |      | text   | for “Page:”     |         |     |     |     |
|     |            |           | \hpword{text}   |         | substitutes |      | text   | for “Points:”   |         |     |     |     |
|     |            |           | \hsword{text}   |         | substitutes |      | text   | for “Score:”    |         |     |     |     |
|     |            |           | \htword{text}   |         | substitutes |      | text   | for “Total”     |         |     |     |     |
| For | vertical   | bonus     | tables:         |         |             |      |        |                 |         |     |     |     |
|     |            |           | Command         |         |             |      | Effect |                 |         |     |     |     |
|     |            |           | \bvqword{text}  |         | substitutes |      | text   | for “Question”  |         |     |     |     |
|     |            |           | \bvpgword{text} |         | substitutes |      | text   | for “Page”      |         |     |     |     |
|     |            |           | \bvpword{text}  |         | substitutes |      | text   | for “Bonus      | Points” |     |     |     |
|     |            |           | \bvsword{text}  |         | substitutes |      | text   | for “Score”     |         |     |     |     |
|     |            |           | \bvtword{text}  |         | substitutes |      | text   | for “Total:”    |         |     |     |     |
| For | horizontal |           | bonus tables:   |         |             |      |        |                 |         |     |     |     |
|     |            |           |                 |         |             | Page | 99     |                 |         |     |     |     |

|                | Command         |         |             | Effect               |          |
| -------------- | --------------- | ------- | ----------- | -------------------- | -------- |
|                | \bhqword{text}  |         | substitutes | text for “Question:” |          |
|                |                 |         | substitutes | for “Page:”          |          |
|                | \bhpgword{text} |         |             | text                 |          |
|                | \bhpword{text}  |         | substitutes | text for “Bonus      | Points:” |
|                | \bhsword{text}  |         | substitutes | text for “Score:”    |          |
|                | \bhtword{text}  |         | substitutes | text for “Total”     |          |
| For vertical   | combined        | tables: |             |                      |          |
|                | Command         |         |             | Effect               |          |
|                | \cvqword{text}  |         | substitutes | text for “Question”  |          |
|                | \cvpgword{text} |         | substitutes | text for “Page”      |          |
|                | \cvpword{text}  |         | substitutes | text for “Points”    |          |
|                | \cvbpword{text} |         | substitutes | text for “Bonus      | Points”  |
|                | \cvsword{text}  |         | substitutes | text for “Score”     |          |
|                | \cvtword{text}  |         | substitutes | text for “Total:”    |          |
| For horizontal | combined        | tables: |             |                      |          |
|                | Command         |         |             | Effect               |          |
|                | \chqword{text}  |         | substitutes | text for “Question:” |          |
|                | \chpgword{text} |         | substitutes | text for “Page:”     |          |
|                | \chpword{text}  |         | substitutes | text for “Points:”   |          |
|                | \chbpword{text} |         | substitutes | text for “Bonus      | Points:” |
|                | \chsword{text}  |         | substitutes | text for “Score:”    |          |
|                | \chtword{text}  |         | substitutes | text for “Total”     |          |
If you don’t use any of these commands then you get the default values, which are defined
| by the commands | in  | the following | table: |     |     |
| --------------- | --- | ------------- | ------ | --- | --- |
|                 |     |               | Page   | 100 |     |

|     |                     | Defaults | for grading | and point          | tables |         |     |
| --- | ------------------- | -------- | ----------- | ------------------ | ------ | ------- | --- |
|     | \hqword{Question:}  |          |             | \vqword{Question}  |        |         |     |
|     | \hpgword{Page:}     |          |             | \vpgword{Page}     |        |         |     |
|     | \hpword{Points:}    |          |             | \vpword{Points}    |        |         |     |
|     | \hsword{Score:}     |          |             | \vsword{Score}     |        |         |     |
|     | \htword{Total}      |          |             | \vtword{Total:}    |        |         |     |
|     | \bhqword{Question:} |          |             | \bvqword{Question} |        |         |     |
|     | \bhpgword{Page:}    |          |             | \bvpgword{Page}    |        |         |     |
|     | \bhpword{Bonus      |          | Points:}    | \bvpword{Bonus     |        | Points} |     |
|     | \bhsword{Score:}    |          |             | \bvsword{Score}    |        |         |     |
|     | \bhtword{Total}     |          |             | \bvtword{Total:}   |        |         |     |
|     | \chqword{Question:} |          |             | \cvqword{Question} |        |         |     |
|     | \chpgword{Page:}    |          |             | \cvpgword{Page}    |        |         |     |
|     | \chpword{Points:}   |          |             | \cvpword{Points}   |        |         |     |
|     | \chbpword{Bonus     |          | Points:}    | \cvbpword{Bonus    |        | Points} |     |
|     | \chsword{Score:}    |          |             | \cvsword{Score}    |        |         |     |
|     | \chtword{Total}     |          |             | \cvtword{Total:}   |        |         |     |
\cellwidth{2em}
\gradetablestretch{1.5}
\setlength{\doublerulesep}{2.0pt}
| For | example, if | you type |     |     |     |     |     |
| --- | ----------- | -------- | --- | --- | --- | --- | --- |
\begin{center}
| \hqword{Aufgabe |     | Nr.:} |     |     |     |     |     |
| --------------- | --- | ----- | --- | --- | --- | --- | --- |
\hpword{Punktzahl:}
\htword{\textbf{Summe}}
| \hsword{Davon |     | erreicht:} |     |     |     |     |     |
| ------------- | --- | ---------- | --- | --- | --- | --- | --- |
\cellwidth{2.2em}
\gradetable[h][questions]
\end{center}
| then you’ll | get  |     |          |     |       |     |       |
| ----------- | ---- | --- | -------- | --- | ----- | --- | ----- |
| Aufgabe     | Nr.: | 1   | 2 3      | 4 5 | 6 7   | 8   | Summe |
| Punktzahl:  |      | 15  | 15 15 15 | 15  | 15 15 | 15  | 120   |
Davon erreicht:
Page 101

10 Changing the page margins
The exam document class arranges things so that you get one inch margins at the top, bot-
tom, and sides no matter what size paper you use, as long as you use the corresponding docu-
mentclassoption(a4paper,a5paper,b5paper,letterpaper,legalpaper,executivepaper,
or landscape). You can change the sizes of these margins by using the commands that
change the size of the printed area.
To change the width of the printed area, you would use the \extrawidth command. The
\extrawidth command takes one argument, and enlarges the width of the printed area by
the amount of the argument. It keeps the printed area centered as it changes its width. If
the argument is negative, then the width of the printed area is decreased.
For example, to enlarge the left and right margins by one half inch each, you would use
the command
\extrawidth{-1in}
since the printed region must shrink by one inch to allow an additional one half inch on both
sides. To decrease the left and right margins to three quarters of an inch each, you would
use the command
\extrawidth{.5in}
since the printed region must grow by one half inch to decrease both margins by one quarter
of an inch.
To change the height of the printed area, you must choose whether the top or the bottom
of the printed area (or possibly both) should move. The commands for this are principally
intended to allow additional room for large headers and footers, and so they are called
\extraheadheight and \extrafootheight. For a full description of these commands, see
section 11.4.
To move the top of the printed region (and any header that’s present) downwards, you
use the command \extraheadheight. This command takes one argument, and moves the
topofthetextandtheheaderdownbythisamount(keepingthedistancebetweentheheader
and the text constant). Thus, to increase the top margin by three quarters of an inch, you
would give the command
\extraheadheight{.75in}
To decrease the top margin by one half inch, you would give the command
\extraheadheight{-.5in}
The \extraheadheight command takes an optional argument to provide a top margin on
the first page that’s different from that on all other pages. For an explanation of this, see
section 11.4.
To move the bottom of the printed region (and any footer that’s present) upwards, you
use the command \extrafootheight. This command takes one argument, and moves the
bottom of the text and the footer up by this amount (keeping the distance between the
footer and the text constant). Thus, to increase the bottom margin by three quarters of an
inch, you would give the command
Page 102

\extrafootheight{.75in}
To decrease the bottom margin by one half inch, you would give the command
\extrafootheight{-.5in}
The \extrafootheight command takes an optional argument to provide a bottom margin
on the first page that’s different from that on all other pages. For an explanation of this, see
section 11.4.
| 11  | Headers |     | and | footers |     |     |
| --- | ------- | --- | --- | ------- | --- | --- |
Thefollowingsectionsexplainallofthecommandsthatdealwithheadersandfooters. There
areanumberofthingstoexplainhere, andsoyoumayfinditeasiertoskipthesesectionsand
instead look at the examples in sections 11.10.1 through 11.10.8 (on pages 117 through 125).
You can then refer back to these sections for the full story on whatever isn’t clear from the
examples. All of the commands described in these sections should be given in the preamble,
i.e., after the \documentclass command and before the \begin{document} command.
It’s also important to remember that if you use a coverpages environment (described
in section 12), then the commands described here affect only the pages in the main section
of the exam, and not the pages of the coverpages environment. There are commands for
headers and footers in the cover pages that are analogous to the commands described in this
| section; | for that, | see     | section | 12.1.   |        |         |
| -------- | --------- | ------- | ------- | ------- | ------ | ------- |
| 11.1     | Page      | styles: |         | Headers | and/or | footers |
It’s the \pagestyle command that determines whether the exam will have headers, footers,
both, or neither. The contents of the header and footer are specified using the commands
described in sections 11.2 through 11.5, but it’s the \pagestyle command that determines
whether the header and footer that you construct will actually be placed onto the page.
The \pagestyle command should be given in the preamble, i.e., after the \documentclass
| command | and       | before | the    | \begin{document} |      | command.    |
| ------- | --------- | ------ | ------ | ---------------- | ---- | ----------- |
| To      | have both | a      | header | and a footer,    | give | the command |
\pagestyle{headandfoot}
If you want every page to have a header but no footer, give the command
\pagestyle{head}
| To give | every | page | a footer | but no | header, | give the command |
| ------- | ----- | ---- | -------- | ------ | ------- | ---------------- |
\pagestyle{foot}
Finally, to omit both the header and the footer from the page, give the command
\pagestyle{empty}
|     |     |     |     |     |     | Page 103 |
| --- | --- | --- | --- | --- | --- | -------- |

As is true for all LATEX document classes, you can change the page style used on a single
| page by | giving the command |     |     |     |     |     |     |     |
| ------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
\thispagestyle{somestyle}
somewhere on that page (where somestyle is the style that you want to use on that page).
This is most often needed if you use the \maketitle command, since that command inserts
a \thispagestyle{plain} immediately following the title. If you use the \maketitle com-
mand and you want the entire document to use \pagestyle{headandfoot}, then you’ll need
| to put the | command |                             |     |     |     | immediately | after the |            |
| ---------- | ------- | --------------------------- | --- | --- | --- | ----------- | --------- | ---------- |
|            |         | \thispagestyle{headandfoot} |     |     |     |             |           | \maketitle |
command to override the \thispagestyle{plain} that is inserted by \maketitle.
The default page style is headandfoot. That is, if you don’t give any \pagestyle
commands, then the header and footer will appear on every page. The default header is
empty, and the default footer consists of “Page n” centered in the footer (where n is the
page number).
| 11.2       | The three    | parts    | of     | the header |     |     |     |     |
| ---------- | ------------ | -------- | ------ | ---------- | --- | --- | --- | --- |
| The header | is specified | in three | parts: |            |     |     |     |     |
•
| One | part to be | left justified. |     |     |     |     |     |     |
| --- | ---------- | --------------- | --- | --- | --- | --- | --- | --- |
•
| One   | part to be | centered.        |     |     |     |     |     |     |
| ----- | ---------- | ---------------- | --- | --- | --- | --- | --- | --- |
| • One | part to be | right justified. |     |     |     |     |     |     |
There are two different ways in which you can specify the three parts of the header. The first
uses the single command \header to specify all three parts of the header, or the commands
\firstpageheader and \runningheader to specify a different header for the first page
(see section 11.2.1). The second uses the commands \lhead, \chead, and \rhead, each of
which can have an optional argument to specify a different header for the first page (see
section 11.2.2). All of these commands should be given in the preamble, i.e., after the
\documentclass command and before the \begin{document} command.
| 11.2.1 | Using \header, | \firstpageheader |     |     | and \runningheader |     |     |     |
| ------ | -------------- | ---------------- | --- | --- | ------------------ | --- | --- | --- |
The command \header{Text 1}{Text 2}{Text 3} puts “Text 1” into the left justified
header, “Text 2” into the centered header, and “Text 3” into the right justified header on
every page. If you want the header on the first page to be different from that on the other
pages, then you should use the commands \firstpageheader and \runningheader, which
also take three arguments and affect either the first page or all pages except the first.
| For example, | to          | put the | header     |        |             |     |     |              |
| ------------ | ----------- | ------- | ---------- | ------ | ----------- | --- | --- | ------------ |
| Math 115     |             |         |            | Second | Exam        |     |     | July 4, 1776 |
| on every     | page of the | exam,   | you would  | give   | the command |     |     |              |
| \header{Math | 115}{Second |         | Exam}{July |        | 4, 1776}    |     |     |              |
|              |             |         |            | Page   | 104         |     |     |              |

If you want to use a header on the first page that’s different from the header used on all
other pages, you would use the commands \firstpageheader and \runningheader instead
of \header. For example, if you want the above header for the first page, but on all pages
| after                 | the first | you want |     | to have     | the    | header     |             |          |     |      |         |
| --------------------- | --------- | -------- | --- | ----------- | ------ | ---------- | ----------- | -------- | --- | ---- | ------- |
| Math                  | 115       |          |     |             | Second | Exam       | (Continued) |          |     | July | 4, 1776 |
| then                  | you would | give     | the | commands    |        |            |             |          |     |      |         |
| \firstpageheader{Math |           |          |     | 115}{Second |        | Exam}{July |             | 4, 1776} |     |      |         |
\runningheader{Math 115}{Second Exam (Continued)}{July 4, 1776}
You can leave one or more of the three parts empty. To have the header
| Math                  | 115   |            |           |               |      | Second       | Exam         |          |        | July             | 4, 1776 |
| --------------------- | ----- | ---------- | --------- | ------------- | ---- | ------------ | ------------ | -------- | ------ | ---------------- | ------- |
| on the                | first | page, with | the       | header        |      |              |              |          |        |                  |         |
| Math                  | 115   |            |           |               |      |              |              |          | Second | Exam (Continued) |         |
| on all                | other | pages,     | you would |               | give | the commands |              |          |        |                  |         |
| \firstpageheader{Math |       |            |           | 115}{Second   |      | Exam}{July   |              | 4, 1776} |        |                  |         |
| \runningheader{Math   |       |            |           | 115}{}{Second |      | Exam         | (Continued)} |          |        |                  |         |
Any of the three parts of the header can have multiple lines. To specify where the line
| breaks                  | should | go, you     | just | type  | \\.  | Thus, to       | have | the header |     |       |         |
| ----------------------- | ------ | ----------- | ---- | ----- | ---- | -------------- | ---- | ---------- | --- | ----- | ------- |
| Math                    | 115    |             |      |       |      |                |      |            |     | First | Exam    |
| Professor               |        | Hilbert     |      |       |      |                |      |            |     | July  | 4, 1776 |
| appear                  | on     | every page, | you  | would | give | the command    |      |            |     |       |         |
| \header{\bfseries\large |        |             |      | Math  |      | 115\\Professor |      | Hilbert}   |     |       |         |
{}
|        | {\bfseries\large |         |     | First  |     | Exam\\July |     | 4, 1776} |     |     |     |
| ------ | ---------------- | ------- | --- | ------ | --- | ---------- | --- | -------- | --- | --- | --- |
| 11.2.2 | Using            | \lhead, |     | \chead | and | \rhead     |     |          |     |     |     |
The command puts “Text” into the left justified part of the header on every
\lhead{Text}
page. The command \lhead[Text 1]{Text 2} puts “Text 1” into the left justified header
onthefirstpageand“Text2”intotheleftjustifiedheaderonallotherpages. Thecommands
\cheadand\rheadhavesimilareffectsonthecenteredandrightjustifiedpartsoftheheader.
| For      | example, | to     | put   | the header |       |        |              |     |     |      |         |
| -------- | -------- | ------ | ----- | ---------- | ----- | ------ | ------------ | --- | --- | ---- | ------- |
| Math     | 115      |        |       |            |       | Second | Exam         |     |     | July | 4, 1776 |
| on every | page     | of the | exam, | you        | would | give   | the commands |     |     |      |         |
|          |          |        |       |            |       | Page   | 105          |     |     |      |         |

| \lhead{Math   |     | 115}     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| \chead{Second |     | Exam}    |     |     |     |     |     |     |     |     |     |
| \rhead{July   |     | 4, 1776} |     |     |     |     |     |     |     |     |     |
If you want any of the three parts to have a special version to be used only on the first
page, then you just include that special version as an optional argument (enclosed in square
brackets) to the command. For example, if you want the above header for the first page, but
| on all pages  | after | the          | first | you      | want   | to have      | the header  |     |     |      |         |
| ------------- | ----- | ------------ | ----- | -------- | ------ | ------------ | ----------- | --- | --- | ---- | ------- |
| Math 115      |       |              |       |          | Second | Exam         | (Continued) |     |     | July | 4, 1776 |
| then you      | would | give         | the   | commands |        |              |             |     |     |      |         |
| \lhead{Math   |       | 115}         |       |          |        |              |             |     |     |      |         |
| \chead[Second |       | Exam]{Second |       |          | Exam   | (Continued)} |             |     |     |      |         |
| \rhead{July   |       | 4, 1776}     |       |          |        |              |             |     |     |      |         |
You can leave one or more of the three parts empty. To have the header
| Math 115      |             |                 |           |        |          | Second       | Exam |     |        | July             | 4, 1776 |
| ------------- | ----------- | --------------- | --------- | ------ | -------- | ------------ | ---- | --- | ------ | ---------------- | ------- |
| on the        | first page, | with            | the       | header |          |              |      |     |        |                  |         |
| Math 115      |             |                 |           |        |          |              |      |     | Second | Exam (Continued) |         |
| on all other  | pages,      |                 | you would |        | give the | commands     |      |     |        |                  |         |
| \lhead{Math   |             | 115}            |           |        |          |              |      |     |        |                  |         |
| \chead[Second |             | Exam]{}         |           |        |          |              |      |     |        |                  |         |
| \rhead[July   |             | 4, 1776]{Second |           |        | Exam     | (Continued)} |      |     |        |                  |         |
Any of the three parts of the header can have multiple lines. To specify where the line
| breaks                 | should   | go, you | just | type  | \\.            | Thus, to     | have the | header   |     |       |         |
| ---------------------- | -------- | ------- | ---- | ----- | -------------- | ------------ | -------- | -------- | --- | ----- | ------- |
| Math                   | 115      |         |      |       |                |              |          |          |     | First | Exam    |
| Professor              |          | Hilbert |      |       |                |              |          |          |     | July  | 4, 1776 |
| appear                 | on every | page,   | you  | would | give           | the commands |          |          |     |       |         |
| \lhead{\bfseries\large |          |         |      | Math  | 115\\Professor |              |          | Hilbert} |     |       |         |
\chead{}
| \rhead{\bfseries\large |     |     |     | First | Exam\\July |      | 4,  | 1776} |     |     |     |
| ---------------------- | --- | --- | --- | ----- | ---------- | ---- | --- | ----- | --- | --- | --- |
|                        |     |     |     |       |            | Page | 106 |       |     |     |     |

| 11.2.3 | Commands |     |     | with optional |     | arguments |     |     |
| ------ | -------- | --- | --- | ------------- | --- | --------- | --- | --- |
LATEX has the property that if a command takes an optional argument, and if that optional
argument contains a command that also has an optional argument, then that inner command
must be enclosed within curly braces. For example, if you want the right justified part of the
| first page | header |     | to be |     |     |     |     |     |
| ---------- | ------ | --- | ----- | --- | --- | --- | --- | --- |
Name:
but you want the right justified part of the header on pages after the first to be empty, then
| you should |     | give the | command |     |     |     |     |     |
| ---------- | --- | -------- | ------- | --- | --- | --- | --- | --- |
\rhead[{Name:\enspace\makebox[2in]{\hrulefill}}]{}
| Note that | the | optional |     | argument | to  | the \rhead | command | is  |
| --------- | --- | -------- | --- | -------- | --- | ---------- | ------- | --- |
{Name:\enspace\makebox[2in]{\hrulefill}}
and not
Name:\enspace\makebox[2in]{\hrulefill}
This is due to the way that LATEX delimits optional arguments, and is nothing special about
| the exam | document |     | class. |              |     |              |     |     |
| -------- | -------- | --- | ------ | ------------ | --- | ------------ | --- | --- |
| Leaving  | extra    |     | room   | for multiple |     | line headers |     |     |
See section 11.4 for a description of the \extraheadheight command.
| 11.3 | The | three |     | parts | of the | footer |     |     |
| ---- | --- | ----- | --- | ----- | ------ | ------ | --- | --- |
The footer is composed of three parts, the whole setup being similar to that for the header
(see section 11.2). There are two different ways in which you can specify the three parts of
the footer. The first uses the single command \footer to specify all three parts of the footer,
or the commands \firstpagefooter and \runningfooter to specify a different footer for
the first page (see section 11.3.1). The second uses the commands \lfoot, \cfoot, and
\rfoot, each of which can have an optional argument to specify a different footer for the
first page (see section 11.3.2). All of these commands should be given in the preamble, i.e.,
after the \documentclass command and before the \begin{document} command.
| 11.3.1 | Using |     | \footer, | \firstpagefooter |     |     | and \runningfooter |     |
| ------ | ----- | --- | -------- | ---------------- | --- | --- | ------------------ | --- |
The command \footer{Text 1}{Text 2}{Text 3} puts “Text 1” into the left justified
footer, “Text 2” into the centered footer and “Text 3” into the right justified footer on every
page. If you want the footer on the first page to be different from that on the other pages,
then you should use the commands \firstpagefooter and \runningfooter, which also
take three arguments and affect either the first page or all pages except the first.
For example, to have an empty footer on the first page and the footer
|     |     |     |     |     |     | Page | 107 |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- |

Page 3 of 5
| on all pages | after the | first, | you would | give the commands |
| ------------ | --------- | ------ | --------- | ----------------- |
\firstpagefooter{}{}{}
| \runningfooter{}{Page |     |     | \thepage\ | of \numpages}{} |
| --------------------- | --- | --- | --------- | --------------- |
(For an explanation of the \numpages command, see section 11.6.)
| 11.3.2 | Using \lfoot, |     | \cfoot, | and \rfoot |
| ------ | ------------- | --- | ------- | ---------- |
The command \lfoot{Text} puts “Text” into the left justified part of the footer on every
page. The command puts “Text 1” into the left justified footer
|     |     | \lfoot[Text |     | 1]{Text 2} |
| --- | --- | ----------- | --- | ---------- |
on the first page and “Text 2” into the left justified footer on all other pages. The commands
\cfoot and \rfoot have similar effects on the centered and right justified parts of the footer.
For example, to have an empty footer on the first page and the footer
Page 3 of 5
| on all pages | after the | first, | you would | give the commands |
| ------------ | --------- | ------ | --------- | ----------------- |
\lfoot{}
\cfoot{}
| \rfoot[]{Page | \thepage\ |     | of \numpages} |     |
| ------------- | --------- | --- | ------------- | --- |
(For an explanation of the \numpages command, see section 11.6.)
| Leaving | extra room | for | multiple | line footers |
| ------- | ---------- | --- | -------- | ------------ |
See section 11.4 for a description of the \extrafootheight command.
11.4 Leaving extra room for multiple line headers and footers
Headers
If you specify more than one or two lines for any part of the header, then you may want
to move the header down slightly so that it doesn’t run off of the top of the paper. The
command for this is \extraheadheight. You can also use the \extraheadheight command
to adjust the size of the text area. The \extraheadheight command never changes the
| distance | between the | header | and the | text. |
| -------- | ----------- | ------ | ------- | ----- |
For example, to move the header and the text an additional half inch down from the top
| of the page, | you would | give | the command |     |
| ------------ | --------- | ---- | ----------- | --- |
\extraheadheight{.5in}
Page 108

You can also specify a negative distance to \extraheadheight to move the header up closer
| to the | top of the paper. | For example, | the command |     |     |
| ------ | ----------------- | ------------ | ----------- | --- | --- |
\extraheadheight{-.25in}
| moves | the header one | quarter inch | closer to the | top of the | paper. |
| ----- | -------------- | ------------ | ------------- | ---------- | ------ |
If you want to have a different value for \extraheadheight on the first page from that
on the pages after the first, then use the same syntax as in the \lhead, \chead, and \rhead
commands (see section 11.2.2): Include an optional argument giving the extra head height
for the first page, and the required argument will apply only to those pages after the first.
| For example, | the command |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- |
\extraheadheight[.5in]{.25in}
gives a half inch of extra head height on the first page and a quarter inch of extra head
| height | on all pages | after the first. |     |     |     |
| ------ | ------------ | ---------------- | --- | --- | --- |
If you give an \extraheadheight command, it should be in the preamble, i.e., after the
\documentclasscommandandbeforethe\begin{document}command. The\extraheadheight
command can also be used to change the size of the text region (see section 10).
Footers
To leave extra room for multiple line footers, you use the command \extrafootheight. To
move the footer one half inch higher up on the paper, you would give the command
\extrafootheight{.5in}
If you wanted to move the footer an eighth of an inch lower down on the paper, you would
| give the | command |     |     |     |     |
| -------- | ------- | --- | --- | --- | --- |
\extrafootheight{-.125in}
If you want to have a different value for \extrafootheight on the first page from that
on the pages after the first, then use the same syntax as in the \lfoot, \cfoot, and \rfoot
commands (see section 11.3.2): Include an optional argument giving the extra foot height
for the first page, and the required argument will apply only to those pages after the first.
| For example, | the command |     |     |     |     |
| ------------ | ----------- | --- | --- | --- | --- |
\extrafootheight[.5in]{.25in}
gives a half inch of extra foot height on the first page and a quarter inch of extra foot height
| on all | pages after the | first. |     |     |     |
| ------ | --------------- | ------ | --- | --- | --- |
If you give an \extrafootheight command, it should be in the preamble, i.e., after the
\documentclasscommandandbeforethe\begin{document}command. The\extrafootheight
command can also be used to change the size of the text region (see section 10).
|     |     |     | Page | 109 |     |
| --- | --- | --- | ---- | --- | --- |

| 11.5 | Horizontal | rules |     |     |
| ---- | ---------- | ----- | --- | --- |
The exam document class make it easy to put a horizontal rule under the header and one
above the footer. It is also easy to do this for the pages after the first page without affecting
| the first | page. |     |     |     |
| --------- | ----- | --- | --- | --- |
• The command \runningheadrule puts a horizontal rule below the header on all pages
| after | the first. |     |     |     |
| ----- | ---------- | --- | --- | --- |
• The command \firstpageheadrule puts a rule under the header of only the first
page.
•
The command \headrule is equivalent to the two commands \firstpageheadrule
| and | \runningheadrule. |     |     |     |
| --- | ----------------- | --- | --- | --- |
•
The command \runningfootrule puts a horizontal rule above the footer on all pages
| after | the first. |     |     |     |
| ----- | ---------- | --- | --- | --- |
• The command \firstpagefootrule puts a rule above the footer of only the first page.
• The command \footrule is equivalent to the two commands \firstpagefootrule
| and          | \runningfootrule. |                    |              |              |
| ------------ | ----------------- | ------------------ | ------------ | ------------ |
| For example, | to have           | the header         |              |              |
| Math 115     |                   |                    | First Exam   | July 4, 1776 |
| on the first | page, with        | the header         |              |              |
| Math 115     |                   |                    | First Exam   | July 4, 1776 |
| on all pages | after the         | first, give either | the commands |              |
\runningheadrule
| \header{Math | 115}{First | Exam}{July | 4, 1776} |     |
| ------------ | ---------- | ---------- | -------- | --- |
or the commands
\runningheadrule
| \lhead{Math  | 115}     |     |     |     |
| ------------ | -------- | --- | --- | --- |
| \chead{First | Exam}    |     |     |     |
| \rhead{July  | 4, 1776} |     |     |     |
For a description of the command \header see section 11.2.1; for a description of the com-
| mands \lhead, | \chead,   | and \rhead,        | see section 11.2.2. |     |
| ------------- | --------- | ------------------ | ------------------- | --- |
| To have       | no footer | on the first page, | and the footer      |     |
Page 3 of 5
Page 110

| on all pages |     | after | the first, | give | the commands |     |     |
| ------------ | --- | ----- | ---------- | ---- | ------------ | --- | --- |
\runningfootrule
\lfoot{}
| \cfoot[]{Page |     | \thepage\ |     | of  | \numpages} |     |     |
| ------------- | --- | --------- | --- | --- | ---------- | --- | --- |
\rfoot{}
(For an explanation of the \numpages command, see section 11.6.)
| 11.6 | Listing |     | the | number | of  | pages | in the exam |
| ---- | ------- | --- | --- | ------ | --- | ----- | ----------- |
The exam document class defines the command \numpages so that it will expand to the
| number         | of pages | in  | the       | exam.       | Thus, to        | have     | the footer |
| -------------- | -------- | --- | --------- | ----------- | --------------- | -------- | ---------- |
|                |          |     |           |             |                 | Page 111 | of 135     |
| you should     | either   |     | give      | the command |                 |          |            |
| \footer{}{Page |          |     | \thepage\ |             | of \numpages}{} |          |            |
or the commands
\lfoot{}
| \cfoot{Page |     | \thepage\ |     | of  | \numpages} |     |     |
| ----------- | --- | --------- | --- | --- | ---------- | --- | --- |
\rfoot{}
For a description of the command \footer see section 11.3.1; for a description of the com-
| mands | \lfoot, | \cfoot, |     | and | \rfoot, | see section | 11.3.2. |
| ----- | ------- | ------- | --- | --- | ------- | ----------- | ------- |
Note that if your document has a coverpages environment (see section 12), then those
pages will not be counted in \numpages; the exam document class defines the command
\numcoverpages so that it will expand to the number of cover pages in the exam. If
there is no coverpages environment, then \numcoverpages expands to 0. The exam class
also defines the command \totalnumpages, which expands to the sum of \numpages and
\numcoverpages. Note that if there are pages preceding a coverpages environment, then
| those pages |     | will not | be  | counted | by \totalnumpages. |     |     |
| ----------- | --- | -------- | --- | ------- | ------------------ | --- | --- |
As with all other cross referencing commands in LATEX, you’ll have to run the file through
LATEX twice to be sure that \numpages, \numcoverpages, and \totalnumpages are correct.
| 11.7 | Treating |     | the | last | page | differently |     |
| ---- | -------- | --- | --- | ---- | ---- | ----------- | --- |
If you want to vary the text that appears in the header or footer on the last page of the
| exam, you | should |     | use the | command | \iflastpage.     |     | The command |
| --------- | ------ | --- | ------- | ------- | ---------------- | --- | ----------- |
|           |        |     |         |         | \iflastpage{Text |     | 1}{Text 2}  |
expands to ‘Text 1’ on the last page and to ‘Text 2’ on all pages before the last. Thus, to
| have the | footer |     |     |     |     |     |     |
| -------- | ------ | --- | --- | --- | --- | --- | --- |
Page 111

|              |           |          | Please   | go on to the | next | page... |
| ------------ | --------- | -------- | -------- | ------------ | ---- | ------- |
| on all pages | before    | the last | page and | the footer   |      |         |
|              |           |          |          | End of       | exam |         |
| on the last  | page, you | should   | give     | the command  |      |         |
\footer{}
{\iflastpage{End of exam}{Please go on to the next page\ldots}}
{}
or the commands
\lfoot{}
\cfoot{\iflastpage{End of exam}{Please go on to the next page\ldots}}
\rfoot{}
For a description of the command \footer see section 11.3.1; for a description of the com-
| mands \lfoot, | \cfoot, | and | \rfoot, | see section | 11.3.2. |     |
| ------------- | ------- | --- | ------- | ----------- | ------- | --- |
As with all other cross referencing commands in LATEX, you’ll have to run the file through
LATEX twice to be sure that \iflastpage correctly detects the last page.
| 11.8 | Treating | odd | and | even numbered |     | pages differently |
| ---- | -------- | --- | --- | ------------- | --- | ----------------- |
If you’d like odd and even numbered pages to be treated differently (perhaps because you’ll
be printing onto both sides of the paper), you should use the command. The
\oddeven
command
|     |     |     | \oddeven{Text |     | 1}{Text | 2}  |
| --- | --- | --- | ------------- | --- | ------- | --- |
expands to ‘Text 1’ on odd numbered pages and to ‘Text 2’ on even numbered pages.
For example, to have the page number printed in the right head on odd numbered pages
and in the left head on even numbered pages, you should give the command
\header{\oddeven{}{\thepage}}%
{}%
{\oddeven{\thepage}{}}
or the commands
\lhead{\oddeven{}{\thepage}}
\rhead{\oddeven{\thepage}{}}
\chead{}
|     |     |     |     | Page | 112 |     |
| --- | --- | --- | --- | ---- | --- | --- |

If you want the footer of the even numbered pages to be empty and the footer of the odd
numbered pages to contain the centered message “Please continue...”, except that the last
page of the exam should have an empty footer whether its page number is even or odd, then
| you | should | give | the | command |     |     |     |     |
| --- | ------ | ---- | --- | ------- | --- | --- | --- | --- |
\footer{}
|     |     | {\oddeven{\iflastpage{}{Please |     |     |     |     | continue\ldots}}{}} |     |
| --- | --- | ------------------------------ | --- | --- | --- | --- | ------------------- | --- |
{}
or the commands
\lfoot{}
\rfoot{}
| \cfoot{\oddeven{\iflastpage{}{Please |         |      |     |                |     |                  | continue\dots}}{}} |     |
| ------------------------------------ | ------- | ---- | --- | -------------- | --- | ---------------- | ------------------ | --- |
| (see                                 | section | 11.7 | for | an explanation |     | of \iflastpage). |                    |     |
The \oddeven command can be used reliably only in headers and footers. This is because
LATEX generally processes more text than can fit on the current page before chooses a page
break it outputs a page. When the \oddeven command is encountered it will act as though
it will appear on the current page whether it will actually be printed on that page or on the
following page; in headers and footers this never creates a problem.
| 11.9 |      | Questions |     | that  | span     | multiple     | pages |     |
| ---- | ---- | --------- | --- | ----- | -------- | ------------ | ----- | --- |
| The  | exam | document  |     | class | provides | the commands |       |     |
• \ifcontinuation and \ContinuedQuestion to enable headers and footers that an-
nounce whether the current page is continuing a question begun on an earlier page
|     | and, | if  | so, the | number | of  | that question | (see section | 11.9.1), and |
| --- | ---- | --- | ------- | ------ | --- | ------------- | ------------ | ------------ |
• \ifincomplete and \IncompleteQuestion to enable headers and footers that an-
nounce whether the question at the bottom of the current page continues onto the
next page and, if so, the number of that question (see section 11.9.2).
These commands are only guaranteed to work reliably in headers and footers. If you use any
of them elsewhere, they may be fooled by LATEX’s practice of typesetting a bit too much
material to fit on a page before it chooses a page break and ships out the page. They also
assume that there is only one questions environment in the entire exam.
| 11.9.1 |     | Questions |     | continuing |     | from the | previous | page |
| ------ | --- | --------- | --- | ---------- | --- | -------- | -------- | ---- |
Headers and footers can announce whether the current page continues a question begun on
| an  | earlier | page. | The | command |                      |     |          |            |
| --- | ------- | ----- | --- | ------- | -------------------- | --- | -------- | ---------- |
|     |         |       |     |         | \ifcontinuation{Text |     |          | 1}{Text 2} |
|     |         |       |     |         |                      |     | Page 113 |            |

expands to ‘Text 1’ if the current page begins with a continuation of a question begun on an
earlier page, and to ‘Text 2’ otherwise. If the current page does continue a question begun
| on an earlier |     | page, then | the | command |     |     |
| ------------- | --- | ---------- | --- | ------- | --- | --- |
\ContinuedQuestion
| expands      | to the         | number | of       | that question. |                |        |
| ------------ | -------------- | ------ | -------- | -------------- | -------------- | ------ |
| For          | example,       | to     | have the | header         |                |        |
|              |                |        |          |                | First Exam     | Page 4 |
| on all pages | that           | begin  | a        | new question   | and the header |        |
| Question     | 6 continues... |        |          |                | First Exam     | Page 4 |
onallpagesthatcontinueaquestionbegunonapreviouspage, youwouldgivethecommands
\lhead{\ifcontinuation{Question \ContinuedQuestion\ continues\ldots}{}}
| \chead{First |     | Exam}     |     |     |     |     |
| ------------ | --- | --------- | --- | --- | --- | --- |
| \rhead{Page  |     | \thepage} |     |     |     |     |
(See section 11.2.2 for an explanation of \lhead, \chead and \rhead.)
The \ifcontinuation command figures out which text to use by checking whether
there is a \question command appearing on the page before any of the commands \part,
\subpart, \subsubpart, \choice, or \CorrectChoice, and this works well for most pages.
However, the \ifcontinuation command can make mistakes on pages on which none of
those commands appear. The default is to assume that a page with none of those commands
continues a question begun on an earlier page, but there are two commands you can use to
tell the \ifcontinuation command that it should not assume that:
• the \nomorequestions command can be used to mark the point at which the last
question ends. This can be useful if you want to include supplementary material (e.g.,
tables or figures) at the end of the exam but you don’t want that material to be
described as continuing the last question. The \nomorequestions command also tells
the \ifincomplete command (see section 11.9.2) that all questions are now complete.
•
The \noquestionsonthispage command tells the \ifcontinuation command (and
the \ifincomplete command; see section 11.9.2) that this page does not continue a
questionbegunonanearlierpage. Thisissimilartothejobdonebythe\nomorequestions
command for the pages that follow the end of all of the questions. Note that if you’re
tempted to use this command on a page that follows the end of all of the questions,
then you should probably use the command \nomorequestions instead.
Thus, in more detail, the command \ifcontinuation{Text 1}{Text 2}
| • expands |     | to ‘Text | 2’  | if  |     |     |
| --------- | --- | -------- | --- | --- | --- | --- |
– a \question appears on this page before any \part, \subpart, \subsubpart,
|     | \choice, |     | or \CorrectChoice, |     | or  |     |
| --- | -------- | --- | ------------------ | --- | --- | --- |
Page 114

– the command \noquestionsonthispage has been given on this page, or
– the current page is before the page containing question number 1, or
– the current page is later than a page with the \nomorequestions command,
| • and  | otherwise |     | it expands |          | to ‘Text | 1’.          |      |     |
| ------ | --------- | --- | ---------- | -------- | -------- | ------------ | ---- | --- |
| 11.9.2 | Questions |     | that       | continue |          | onto a later | page |     |
Headers and footers can announce whether a question on the current page continues onto a
| later page. | The | command |     |                    |     |     |         |     |
| ----------- | --- | ------- | --- | ------------------ | --- | --- | ------- | --- |
|             |     |         |     | \ifincomplete{Text |     |     | 1}{Text | 2}  |
expands to ‘Text 1’ if the last question begun on or before the current page continues onto
a page after this one, and to ‘Text 2’ otherwise. If the last question begun on or before the
| current | page | does continue |     | onto | a later | page, then | the command |     |
| ------- | ---- | ------------- | --- | ---- | ------- | ---------- | ----------- | --- |
\IncompleteQuestion
| expands      | to the | number | of       | that   | question. |                |     |     |
| ------------ | ------ | ------ | -------- | ------ | --------- | -------------- | --- | --- |
| For example, |        | to     | have the | footer |           |                |     |     |
|              |        |        |          |        | Question  | 3 continues... |     |     |
on all pages that end with a question that will be continued onto the next page, the footer
|              |        |     |       |        |     | End of Exam       |     |     |
| ------------ | ------ | --- | ----- | ------ | --- | ----------------- | --- | --- |
| on the last  | page,  | and | the   | footer |     |                   |     |     |
|              |        |     |       |        |     | Exam continues... |     |     |
| on all other | pages, | you | would | give   | the | commands          |     |     |
\footrule
\lfoot{}
\newcommand{\continues}{\ifincomplete
|                        |     |     |     | {Question |                    | \IncompleteQuestion\ |     | continues\ldots} |
| ---------------------- | --- | --- | --- | --------- | ------------------ | -------------------- | --- | ---------------- |
|                        |     |     |     | {Exam     | continues\ldots}}  |                      |     |                  |
| \cfoot{\iflastpage{End |     |     |     | of        | Exam}{\continues}} |                      |     |                  |
\rfoot{}
(See section 11.3.2 for an explanation of \lfoot, \cfoot and \rfoot, and section 11.7 for
| an explanation |     | of \iflastpage). |     |     |     |     |     |     |
| -------------- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
There are two situations in which you may have to give an additional command for the
\ifincomplete command to correctly decide if the current question is incomplete:
|     |     |     |     |     |     | Page 115 |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --- |

1. The \ifincomplete command expands to ‘Text 2’ if there is a \part, \subpart,
\subsubpart, \choice, or \CorrectChoice command belonging to this question on
the following page. For those situations in which the current question flows onto the
nextpage,butthereisno\part,\subpart,\subsubpart,\choice,or\CorrectChoice
belonging to this question on that page, you should give the command
\addquestionobject
at the end of the text of the question to inform the \ifincomplete command that
some portion of the question appears on that following page.
2. If there are pages on which none of those commands appear, the default is to assume
that that page continues a question begun on an earlier page. There are two commands
that you can use to tell the \ifincomplete command that it should not assume that:
• the \nomorequestions command can be used to mark the point at which the last
question ends. This can be useful if you want to include supplementary material
(e.g., tablesorfigures)attheendoftheexambutyoudon’twantthelastquestion
on the exam to be described as incomplete. The \nomorequestions command
also tells the \ifcontinuation command (see section 11.9.1) that all questions
are now complete.
• The\noquestionsonthispagecommandtellsthe\ifincompletecommand(and
the \ifcontinuation command; see section 11.9.1) that this page does not con-
tain any incomplete questions, and does not continue a question begun on an
earlier page. This is similar to the job done by the \nomorequestions command
forthepagesthatfollowtheendofallofthequestions. Notethatifyou’retempted
to use this command on a page that follows the end of all of the questions, then
you should probably use the command \nomorequestions instead.
If you give the command \noquestionsonthispage on a page, then
• an \ifcontinuation command on that page will expand to its second argument,
• an \ifincomplete on that page will expand to its second argument, and
• an \ifincomplete command on an earlier page will not assume that a question from
that earlier page continues onto this page.
The way that this command affects the \ifincomplete command on earlier pages is as
follows: If there is a page with no \question, \part, \subpart, \subsubparts, \choice,
\CorrectChoice, or \addquestionobject commands, then the last page before that with
a \question (or \part, etc.) would normally be deemed to have an incomplete question; if,
however, the page with no \question (or \part, etc.) (along with all adjacent pages with
no \question or \part etc.) has a \noquestionsonthispage command, then that last page
with a \question (or \part, etc.) will not be deemed incomplete.
Page 116

| 11.10        | Examples   |     |        |       |       |      |        |              |
| ------------ | ---------- | --- | ------ | ----- | ----- | ---- | ------ | ------------ |
| 11.10.1      | Example:   |     |        |       |       |      |        |              |
| To have      | the header |     |        |       |       |      |        |              |
| Math 115     |            |     |        |       | First | Exam |        | July 4, 1776 |
| on the first | page,      | the | header |       |       |      |        |              |
| Math 115     |            |     |        | First | Exam, | Page | 2 of 5 | July 4, 1776 |
on all pages after the first, and no footer on any page, give the commands
\pagestyle{head}
\runningheadrule
| \firstpageheader{Math |     |        |            | 115}{First   | Exam}{July |     | 4, 1776}      |     |
| --------------------- | --- | ------ | ---------- | ------------ | ---------- | --- | ------------- | --- |
| \runningheader{Math   |     |        | 115}       |              |            |     |               |     |
|                       |     | {First | Exam,      | Page         | \thepage\  |     | of \numpages} |     |
|                       |     | {July  | 4,         | 1776}        |            |     |               |     |
| Alternatively,        |     | you    | could give | the commands |            |     |               |     |
\pagestyle{head}
\runningheadrule
| \lhead{Math  |     | 115}        |       |       |      |           |               |     |
| ------------ | --- | ----------- | ----- | ----- | ---- | --------- | ------------- | --- |
| \chead[First |     | Exam]{First |       | Exam, | Page | \thepage\ | of \numpages} |     |
| \rhead{July  |     | 4,          | 1776} |       |      |           |               |     |
Page 117

| 11.10.2     | Example: |     |            |     |         |      |
| ----------- | -------- | --- | ---------- | --- | ------- | ---- |
| To have the | header   |     |            |     |         |      |
| Math 115    |          |     | First Exam |     | July 4, | 1776 |
on the first page, no header on the pages after the first, no footer on the first page, and the
footer
| Math 115     |           |                 | First Exam |     | Page 2 | of 5 |
| ------------ | --------- | --------------- | ---------- | --- | ------ | ---- |
| on all pages | after the | first, give the | commands   |     |        |      |
\pagestyle{headandfoot}
\runningfootrule
| \firstpageheader{Math |     | 115}{First | Exam}{July | 4, 1776} |     |     |
| --------------------- | --- | ---------- | ---------- | -------- | --- | --- |
\runningheader{}{}{}
\firstpagefooter{}{}{}
\runningfooter{Math 115}{First Exam}{Page \thepage\ of \numpages}
| Alternatively, | you could | give the commands |     |     |     |     |
| -------------- | --------- | ----------------- | --- | --- | --- | --- |
\pagestyle{headandfoot}
\runningfootrule
| \lhead[Math    | 115]{}     |               |     |     |     |     |
| -------------- | ---------- | ------------- | --- | --- | --- | --- |
| \chead[First   | Exam]{}    |               |     |     |     |     |
| \rhead[July    | 4, 1776]{} |               |     |     |     |     |
| \lfoot[]{Math  | 115}       |               |     |     |     |     |
| \cfoot[]{First | Exam}      |               |     |     |     |     |
| \rfoot[]{Page  | \thepage\  | of \numpages} |     |     |     |     |
Page 118

| 11.10.3     | Example:    |      |         |     |     |       |
| ----------- | ----------- | ---- | ------- | --- | --- | ----- |
| To have     | the header  |      |         |     |     |       |
| Mathematics |             | 115  |         |     |     |       |
| First       | Exam,       | July | 4, 1776 |     |     | Name: |
| on the      | first page, | the  | header  |     |     |       |
| Mathematics |             | 115  |         |     |     |       |
| First       | Exam,       | July | 4, 1776 |     |     |       |
on all pages after the first, an empty footer on the first page, and the footer
|        |             |     |                 | Page     | 2   |     |
| ------ | ----------- | --- | --------------- | -------- | --- | --- |
| on all | pages after | the | first, give the | commands |     |     |
\pagestyle{headandfoot}
| \firstpageheader{\large\bfseries |     |     |             | Mathematics |       | 115\\ |
| -------------------------------- | --- | --- | ----------- | ----------- | ----- | ----- |
|                                  |     |     | First Exam, | July 4,     | 1776} |       |
{}
|                                |     | {\large\bfseries |       | Name:\enspace\makebox[2in]{\hrulefill}} |     |       |
| ------------------------------ | --- | ---------------- | ----- | --------------------------------------- | --- | ----- |
| \runningheader{\large\bfseries |     |                  |       | Mathematics                             |     | 115\\ |
|                                |     | First            | Exam, | July 4, 1776}{}{}                       |     |       |
\firstpagefooter{}{}{}
| \runningfooter{}{Page |     |           | \thepage}{} |          |     |     |
| --------------------- | --- | --------- | ----------- | -------- | --- | --- |
| Alternatively,        |     | you could | give the    | commands |     |     |
\pagestyle{headandfoot}
\lhead{\large\bfseries Mathematics 115\\ First Exam, July 4, 1776}
\chead{}
\rhead[{\large\bfseries Name:\enspace\makebox[2in]{\hrulefill}}]{}
\lfoot{}
| \cfoot[]{Page |     | \thepage} |     |     |     |     |
| ------------- | --- | --------- | --- | --- | --- | --- |
\rfoot{}
(For an explanation of why there seems to be an extra pair of curly braces in the optional
| argument | to the | \rhead | command, | see section | 11.2.3.) |     |
| -------- | ------ | ------ | -------- | ----------- | -------- | --- |
|          |        |        |          | Page        | 119      |     |

| 11.10.4      | Example:   |            |             |                    |             |        |          |                  |
| ------------ | ---------- | ---------- | ----------- | ------------------ | ----------- | ------ | -------- | ---------------- |
| To have      | the header |            |             |                    |             |        |          |                  |
|              |            |            |             | Wellesley          | College     |        |          |                  |
|              |            | Second     | Semester    | Final Examination, |             | Spring | 1993     |                  |
|              |            |            |             | Mathematics        | 115         |        |          |                  |
| on the first | page,      | the header |             |                    |             |        |          |                  |
|              |            |            |             | Wellesley          | College     |        |          |                  |
|              |            | Second     | Semester    | Final Examination, |             | Spring | 1993     |                  |
|              |            |            | Mathematics | 115                | (Continued) |        |          |                  |
| on all pages | after      | the first, | the footer  |                    |             |        |          |                  |
|              |            |            |             | Page 3             | of 10       | Please | go on to | the next page... |
| on all pages | except     | the last   | page, and   | the footer         |             |        |          |                  |
|              |            |            |             | Page 10            | of 10       |        |          | End of exam.     |
| on the last  | page,      | give the   | commands    |                    |             |        |          |                  |
\pagestyle{headandfoot}
\extraheadheight{.25in}
\firstpageheader{}
|     |     | {Wellesley  | College\\ |       |              |     |               |     |
| --- | --- | ----------- | --------- | ----- | ------------ | --- | ------------- | --- |
|     |     | Second      | Semester  | Final | Examination, |     | Spring 1993\\ |     |
|     |     | Mathematics |           | 115}  |              |     |               |     |
{}
\runningheader{}
|     |     | {Wellesley  | College\\ |                    |     |        |        |     |
| --- | --- | ----------- | --------- | ------------------ | --- | ------ | ------ | --- |
|     |     | Second      | Semester  | Final Examination, |     | Spring | 1993\\ |     |
|     |     | Mathematics | 115       | (Continued)}       |     |        |        |     |
{}
\footer{}
|     | {Page | \thepage\ | of \numpages} |     |     |     |     |     |
| --- | ----- | --------- | ------------- | --- | --- | --- | --- | --- |
{\iflastpage{End of exam.}{Please go on to the next page\ldots}}
| Alternatively, | you | could | give the commands |     |     |     |     |     |
| -------------- | --- | ----- | ----------------- | --- | --- | --- | --- | --- |
\pagestyle{headandfoot}
\extraheadheight{.25in}
\lhead{}
| \chead[Wellesley |     | College\\ |     |      |     |     |     |     |
| ---------------- | --- | --------- | --- | ---- | --- | --- | --- | --- |
|                  |     |           |     | Page | 120 |     |     |     |

| Second      | Semester  | Final Examination, | Spring 1993\\ |
| ----------- | --------- | ------------------ | ------------- |
| Mathematics |           | 115]               |               |
| {Wellesley  | College\\ |                    |               |
| Second      | Semester  | Final Examination, | Spring 1993\\ |
| Mathematics |           | 115 (Continued)}   |               |
\rhead{}
\lfoot{}
| \cfoot{Page | \thepage\ | of \numpages} |     |
| ----------- | --------- | ------------- | --- |
\rfoot{\iflastpage{End of exam.}{Please go on to the next page\ldots}}
Page 121

| 11.10.5     | Example:     |             |            |          |                    |         |        |          |                  |
| ----------- | ------------ | ----------- | ---------- | -------- | ------------------ | ------- | ------ | -------- | ---------------- |
| To have     | the header   |             |            |          |                    |         |        |          |                  |
|             |              |             |            |          | Wellesley          | College |        |          |                  |
|             |              | Second      |            | Semester | Final Examination, |         | Spring | 1993     |                  |
|             |              |             |            |          | Mathematics        | 115     |        |          |                  |
| on the      | first page,  | the header  |            |          |                    |         |        |          |                  |
| Mathematics | 115          | (Continued) |            |          |                    |         |        |          | Spring, 1993     |
| on all      | pages after  | the first,  | the        | footer   |                    |         |        |          |                  |
|             |              |             |            |          | Page 3             | of 10   | Please | go on to | the next page... |
| on all      | pages except | the         | last page, | and      | the footer         |         |        |          |                  |
|             |              |             |            |          | Page 10            | of 10   |        |          | End of exam.     |
| on the      | last page,   | give the    | commands   |          |                    |         |        |          |                  |
\pagestyle{headandfoot}
\extraheadheight[.25in]{}
\firstpageheader{}
|     |     | {Wellesley  |     | College\\ |       |              |     |               |     |
| --- | --- | ----------- | --- | --------- | ----- | ------------ | --- | ------------- | --- |
|     |     | Second      |     | Semester  | Final | Examination, |     | Spring 1993\\ |     |
|     |     | Mathematics |     |           | 115}  |              |     |               |     |
{}
| \runningheader{Mathematics |     |     |     | 115 | (Continued)}{}{Spring, |     |     | 1993} |     |
| -------------------------- | --- | --- | --- | --- | ---------------------- | --- | --- | ----- | --- |
\footer{}
|     | {Page \thepage\ |     | of  | \numpages} |     |     |     |     |     |
| --- | --------------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
{\iflastpage{End of exam.}{Please go on to the next page\ldots}}
| Alternatively, | you | could | give | the commands |     |     |     |     |     |
| -------------- | --- | ----- | ---- | ------------ | --- | --- | --- | --- | --- |
\pagestyle{headandfoot}
\extraheadheight[.25in]{}
| \lhead[]{Mathematics |             |           | 115  | (Continued)} |              |        |        |     |     |
| -------------------- | ----------- | --------- | ---- | ------------ | ------------ | ------ | ------ | --- | --- |
| \chead[Wellesley     |             | College\\ |      |              |              |        |        |     |     |
|                      | Second      | Semester  |      | Final        | Examination, | Spring | 1993\\ |     |     |
|                      | Mathematics |           | 115] |              |              |        |        |     |     |
{}
| \rhead[]{Spring, |     | 1993} |     |     |     |     |     |     |     |
| ---------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
\lfoot{}
| \cfoot{Page | \thepage\ |     | of  | \numpages} |     |     |     |     |     |
| ----------- | --------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
\rfoot{\iflastpage{End of exam.}{Please go on to the next page\ldots}}
|     |     |     |     |     | Page | 122 |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |

| 11.10.6  |       | Example:     |        |     |     |            |     |     |     |         |       |
| -------- | ----- | ------------ | ------ | --- | --- | ---------- | --- | --- | --- | ------- | ----- |
| To have  | the   | header       |        |     |     |            |     |     |     |         |       |
| Math     | 115   |              |        |     |     | First Exam |     |     |     | July 4, | 1776  |
| on the   | first | page, the    | header |     |     |            |     |     |     |         |       |
| Question | 3     | continues... |        |     |     | First Exam |     |     |     | Page 3  | of 10 |
on all pages after the first that continue a question begun on an earlier page, the header
|     |     |     |     |     |     | First Exam |     |     |     | Page 3 | of 10 |
| --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | ------ | ----- |
on all pages after the first that don’t continue a question begun on an earlier page, the footer
|     |     |     |     |     |     |     | Question | 6 continues | on the | next page... |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----------- | ------ | ------------ | --- |
on all pages whose last question continues onto the following page, and no footer on pages
that don’t have a question that continues onto the following page, give the commands
\pagestyle{headandfoot}
\runningheadrule
\newcommand{\continuedmessage}{%
\ifcontinuation{Question \ContinuedQuestion\ continues\ldots}{}%
}
| \firstpageheader{Math |     |     |     | 115}{First |     | Exam}{July | 4, 1776} |     |     |     |     |
| --------------------- | --- | --- | --- | ---------- | --- | ---------- | -------- | --- | --- | --- | --- |
\runningheader{\continuedmessage}
|     |     | {First | Exam}     |     |     |            |     |     |     |     |     |
| --- | --- | ------ | --------- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|     |     | {Page  | \thepage\ |     | of  | \numpages} |     |     |     |     |     |
\footer{}
{}
|                | {\ifincomplete{Question |        |                     |     | \IncompleteQuestion\ |     |     | continues |     |     |     |
| -------------- | ----------------------- | ------ | ------------------- | --- | -------------------- | --- | --- | --------- | --- | --- | --- |
|                |                         | on the | next page\ldots}{}} |     |                      |     |     |           |     |     |     |
| Alternatively, |                         | you    | could give          | the | commands             |     |     |           |     |     |     |
\pagestyle{headandfoot}
\runningheadrule
\newcommand{\continuedmessage}{%
\ifcontinuation{Question \ContinuedQuestion\ continues\ldots}{}%
}
| \lhead[Math  |     | 115]{\continuedmessage} |            |           |     |     |            |     |     |     |     |
| ------------ | --- | ----------------------- | ---------- | --------- | --- | --- | ---------- | --- | --- | --- | --- |
| \chead[First |     | Exam]{First             |            | Exam}     |     |     |            |     |     |     |     |
| \rhead[July  |     | 4,                      | 1776]{Page | \thepage\ |     | of  | \numpages} |     |     |     |     |
\lfoot{}
\cfoot{}
| \rfoot{\ifincomplete{Question |     |     |                     |     | \IncompleteQuestion\ |      |     | continues |     |     |     |
| ----------------------------- | --- | --- | ------------------- | --- | -------------------- | ---- | --- | --------- | --- | --- | --- |
|                               | on  | the | next page\ldots}{}} |     |                      |      |     |           |     |     |     |
|                               |     |     |                     |     |                      | Page | 123 |           |     |     |     |

| 11.10.7  | Example:    |     |        |     |     |             |     |     |     |              |
| -------- | ----------- | --- | ------ | --- | --- | ----------- | --- | --- | --- | ------------ |
| To have  | the header  |     |        |     |     |             |     |     |     |              |
| Math 115 |             |     |        |     |     | Second Exam |     |     |     | July 4, 1776 |
| on the   | first page, | the | header |     |     |             |     |     |     |              |
| Second   | Exam        |     |        |     |     |             |     |     |     | July 4, 1776 |
on all pages after the first, no footer on the first page, and the footer
| Page 3 | of 5        |     |            |      |     |          |     |     | Points        | earned:   |
| ------ | ----------- | --- | ---------- | ---- | --- | -------- | --- | --- | ------------- | --------- |
|        |             |     |            |      |     |          |     | out | of a possible | 20 points |
| on all | pages after |     | the first, | give | the | commands |     |     |               |           |
\pagestyle{headandfoot}
| \firstpageheader{Math |     |     |     | 115}{Second  |     | Exam}{July    | 4, 1776} |     |     |     |
| --------------------- | --- | --- | --- | ------------ | --- | ------------- | -------- | --- | --- | --- |
| \runningheader{Second |     |     |     | Exam}{}{July |     | 4, 1776}      |          |     |     |     |
| \runningfooter{Page   |     |     |     | \thepage\    |     | of \numpages} |          |     |     |     |
{}
|                |     | {Points |       | earned:  |          | \makebox[.5in]{\hrulefill}\\ |     |     |         |     |
| -------------- | --- | ------- | ----- | -------- | -------- | ---------------------------- | --- | --- | ------- | --- |
|                |     |         | out   | of a     | possible | \pointsonpage{\thepage}      |     |     | points} |     |
| Alternatively, |     | you     | could | give the | commands |                              |     |     |         |     |
\pagestyle{headandfoot}
| \lhead[Math   |     | 115]{Second |       | Exam} |            |     |     |     |     |     |
| ------------- | --- | ----------- | ----- | ----- | ---------- | --- | --- | --- | --- | --- |
| \chead[Second |     | Exam]{}     |       |       |            |     |     |     |     |     |
| \rhead{July   |     | 4,          | 1776} |       |            |     |     |     |     |     |
| \lfoot[]{Page |     | \thepage\   |       | of    | \numpages} |     |     |     |     |     |
\cfoot{}
| \rfoot[]{Points |     |     | earned:    | \makebox[.5in]{\hrulefill}\\ |                         |          |     |         |     |     |
| --------------- | --- | --- | ---------- | ---------------------------- | ----------------------- | -------- | --- | ------- | --- | --- |
|                 | out | of  | a possible |                              | \pointsonpage{\thepage} |          |     | points} |     |     |
|                 |     |     |            |                              |                         | Page 124 |     |         |     |     |

| 11.10.8    | Example:       |            |       |     |            |        |     |              |
| ---------- | -------------- | ---------- | ----- | --- | ---------- | ------ | --- | ------------ |
| To have    | the header     |            |       |     |            |        |     |              |
| Math 115   |                |            |       |     | Second     | Exam   |     | July 4, 1776 |
| on the     | first page,    | the header |       |     |            |        |     |              |
|            |                |            |       |     | Second     | Exam   |     | July 4, 1776 |
| on all odd | numbered       | pages      | after | the | first, the | header |     |              |
| Question   | 3 continues... |            |       |     | Math       | 115    |     |              |
on all even numbered pages that continue a question begun on an earlier page, the header
|     |     |     |     |     | Math | 115 |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- |
on all even numbered pages that don’t continue a question begun on an earlier page, the
footer
Page 5 of 10
Question 6 continues...
on all odd numbered pages that have a question that continues onto the following page, the
footer
Page 5 of 10
on all odd numbered pages that don’t have a question that continues onto the following page,
| and the     | footer   |        |      |     |          |     |     |     |
| ----------- | -------- | ------ | ---- | --- | -------- | --- | --- | --- |
| Page 4      | of 10    |        |      |     |          |     |     |     |
| on all even | numbered | pages, | give | the | commands |     |     |     |
\pagestyle{headandfoot}
\newcommand{\continuedmessage}{%
\ifcontinuation{Question \ContinuedQuestion\ continues\ldots}{}%
}
\newcommand{\oddrightfoot}{%
| \ifincomplete{Page |     |          | \thepage\ |                      | of \numpages\\ |     |                   |     |
| ------------------ | --- | -------- | --------- | -------------------- | -------------- | --- | ----------------- | --- |
|                    |     | Question |           | \IncompleteQuestion\ |                |     | continues\ldots}% |     |
|                    |     | {Page    | \thepage\ |                      | of \numpages}  |     |                   |     |
}
| \firstpageheader{Math |     |     | 115}{Second |     | Exam}{July |     | 4, 1776} |     |
| --------------------- | --- | --- | ----------- | --- | ---------- | --- | -------- | --- |
|                       |     |     |             |     | Page       | 125 |          |     |

\runningheader{\oddeven{}{\continuedmessage}}
|                         |     | {\oddeven{Second |           | Exam}{Math     | 115}} |     |
| ----------------------- | --- | ---------------- | --------- | -------------- | ----- | --- |
|                         |     | {\oddeven{July   |           | 4, 1776}{}}    |       |     |
| \footer{\oddeven{}{Page |     |                  | \thepage\ | of \numpages}} |       |     |
{}
{\oddeven{\oddrightfoot}{}}
| Alternatively, | you | could | give the commands |     |     |     |
| -------------- | --- | ----- | ----------------- | --- | --- | --- |
\pagestyle{headandfoot}
\newcommand{\continuedmessage}{%
\ifcontinuation{Question \ContinuedQuestion\ continues\ldots}{}%
}
\newcommand{\oddrightfoot}{%
| \ifincomplete{Page |     |          | \thepage\            | of \numpages\\ |     |                   |
| ------------------ | --- | -------- | -------------------- | -------------- | --- | ----------------- |
|                    |     | Question | \IncompleteQuestion\ |                |     | continues\ldots}% |
|                    |     | {Page    | \thepage\            | of \numpages}  |     |                   |
}
| \lhead[Math            | 115]{\oddeven{}{\continuedmessage}} |     |             |                |     |     |
| ---------------------- | ----------------------------------- | --- | ----------- | -------------- | --- | --- |
| \chead{\oddeven{Second |                                     |     | Exam}{Math  | 115}}          |     |     |
| \rhead{\oddeven{July   |                                     |     | 4, 1776}{}} |                |     |     |
| \lfoot{\oddeven{}{Page |                                     |     | \thepage\   | of \numpages}} |     |     |
\cfoot{}
\rfoot{\oddeven{\oddrightfoot}{}}
| 12 Cover |     | pages |     |     |     |     |
| -------- | --- | ----- | --- | --- | --- | --- |
There is a coverpages environment that allows you to have one or more pages before page 1
of the exam. By default, there are no headers or footers printed on the cover pages, but if
you put the page number into the headers and/or footers (using the commands described in
section 12.1), the page numbers of cover pages are printed in roman numerals.
The coverpages environment must begin and end before the beginning of the questions
| environment. | You | begin | the environment | with | the command |     |
| ------------ | --- | ----- | --------------- | ---- | ----------- | --- |
\begin{coverpages}
| and you end | it with | the | command |     |     |     |
| ----------- | ------- | --- | ------- | --- | --- | --- |
\end{coverpages}
In between those two commands you can put whatever you want, except that you are not
allowed to begin the questions environment until you’ve ended the coverpages environ-
ment. The command \begin{coverpages} sets the page number to 1 and causes any page
numbers printed (using the commands described in section 12.1) to appear as roman numer-
als. The command \end{coverpages} causes the current page to end, sets the page number
of the following page to 1, and changes page numbering back to arabic numerals.
|     |     |     |     | Page | 126 |     |
| --- | --- | --- | --- | ---- | --- | --- |

| 12.1 | Headers | and | footers |     |     |     |     |
| ---- | ------- | --- | ------- | --- | --- | --- | --- |
By default, the headers and footers on the cover pages are empty. If you’d like to have
headers and/or footers on the cover pages, there are commands to create them that are
completely analogous to the commands described in section 11 for headers and footers in
the main part of the document. The commands for headers and footers in cover pages and
| the corresponding |     | commands              | for      | the main | exam | pages are:       |          |
| ----------------- | --- | --------------------- | -------- | -------- | ---- | ---------------- | -------- |
|                   |     | Cover Pages           | Commands |          |      | Main Pages       | Commands |
|                   |     | \coverheader          |          |          |      | \header          |          |
|                   |     | \coverrunningheader   |          |          |      | \runningheader   |          |
|                   |     | \coverfirstpageheader |          |          |      | \firstpageheader |          |
|                   |     | \coverlhead           |          |          |      | \lhead           |          |
|                   |     | \coverchead           |          |          |      | \chead           |          |
|                   |     | \coverrhead           |          |          |      | \rhead           |          |
|                   |     | \coverfooter          |          |          |      | \footer          |          |
|                   |     | \coverrunningfooter   |          |          |      | \runningheader   |          |
|                   |     | \coverfirstpagefooter |          |          |      | \firstpageheader |          |
|                   |     | \coverlfoot           |          |          |      | \lfoot           |          |
|                   |     | \covercfoot           |          |          |      | \cfoot           |          |
|                   |     | \coverrfoot           |          |          |      | \rfoot           |          |
|                   |     | \coverextraheadheight |          |          |      | \extraheadheight |          |
|                   |     | \coverextrafootheight |          |          |      | \extrafootheight |          |
The commands \coverlhead, \coverchead, \coverrhead, \coverlfoot, \covercfoot,
\coverrfoot, \coverextraheadheight, and \coverextrafootheight all all take the same
optional arguments (for special treatment of page number 1) as the corresponding commands
for the main pages. For an explanation of these commands, see section 11.
| 12.2 | Listing | the number |     | of  | cover | pages |     |
| ---- | ------- | ---------- | --- | --- | ----- | ----- | --- |
The exam document class defines the command \numcoverpages so that it will expand
to the number of cover pages in the exam. If there is no coverpages environment, then
expands to 0. The class also defines the command \totalnumpages,
| \numcoverpages |     |     |     | exam |     |     |     |
| -------------- | --- | --- | --- | ---- | --- | --- | --- |
which expands to the sum of \numpages and \numcoverpages. Note: if there are pages pre-
cedingacoverpagesenvironment, thenthosepageswillnotbecountedby\totalnumpages.
| For an       | example, | to have    | the footer |      |             |       |     |
| ------------ | -------- | ---------- | ---------- | ---- | ----------- | ----- | --- |
|              |          |            |            |      | Page ii     | of iv |     |
| on all cover | pages    | you should | either     | give | the command |       |     |
\coverfooter{}{Page \thepage\ of \romannumeral\numcoverpages}{}
|     |     |     |     |     | Page 127 |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- |

or the commands
\coverlfoot{}
\covercfoot{Page \thepage\ of \romannumeral\numcoverpages}
\coverrfoot{}
As with all other cross referencing commands in LATEX, you’ll have to run the file through
LATEX twice to be sure that \numpages, \numcoverpages, and \totalnumpages are correct.
Page 128

Index
\addpoints, 12, 29, 30, 33, 37, 38, 83, 93, 94 \bonusquestion, 35, 36
addpoints, 12, 29, 33, 37, 38, 83, 93, 94 \bonussubpart, 35, 36
| \addquestionobject, |        |     | 116 |     | \bonussubsubpart,     |     |     | 35, | 36     |
| ------------------- | ------ | --- | --- | --- | --------------------- | --- | --- | --- | ------ |
| allocating          | space, |     | 10  |     | \bonustitledquestion, |     |     |     | 35, 36 |
| \Alph,              | 40     |     |     |     | \bonustotalformat,    |     |     | 31, | 37     |
| \alph,              | 40     |     |     |     | \Box,                 | 49  |     |     |        |
| amssymb,            | 49     |     |     |     | \boxedpoints,         |     | 20, | 22, | 23, 26 |
answer space, 9, 55–68, 75–79 \bracketedpoints, 20, 22, 23, 27, 30
| \answerclearance,       |         |           | 48,     | 67         | \bvpgword,       |              | 99        |         |            |
| ----------------------- | ------- | --------- | ------- | ---------- | ---------------- | ------------ | --------- | ------- | ---------- |
| \answerline,            |         | 13,       | 42, 44, | 65–68      | \bvpword,        | 99           |           |         |            |
| optional                |         | argument, | 13,     | 42, 67     | \bvqword,        | 99           |           |         |            |
| \answerlinelength,      |         |           | 65      |            | \bvsword,        | 99           |           |         |            |
| answers,                | 68–82   |           |         |            | \bvtword,        | 99           |           |         |            |
| to                      | short   | answers,  | 67–68   |            |                  |              |           |         |            |
|                         |         |           |         |            | \cancelspace,    |              | 77–78     |         |            |
| answers,                | 12,     | 45,       | 68, 71  |            |                  |              |           |         |            |
|                         |         |           |         |            | cancelspace,     |              | 77        |         |            |
| \answerskip,            |         | 65        |         |            |                  |              |           |         |            |
| \arabic,                | 40      |           |         |            | \cellwidth,      |              | 99,       | 100     |            |
|                         |         |           |         |            | \cfoot,          | 108,         | 117–126   |         |            |
| \baselinestretch,       |         |           | 99      |            | \chbpword,       |              | 100       |         |            |
| \begingradingrange,     |         |           | 91–92,  | 95         | \chead,          | 105–106,     |           | 117–126 |            |
| beta test,              | 6       |           |         |            | different        |              | on first  | page,   | 105        |
| \bhpgword,              |         | 99        |         |            | optional         |              | argument, |         | 105        |
| \bhpword,               | 99      |           |         |            | checkbox,        | 49           |           |         |            |
| \bhqword,               | 99      |           |         |            | \checkboxchar,   |              |           | 49      |            |
| \bhsword,               | 99      |           |         |            | checkboxes,      |              | 13,       | 42, 44, | 45, 48, 49 |
| \bhtword,               | 99      |           |         |            | checkboxes       | environment, |           |         | 42, 44     |
| \blacksquare,           |         | 49        |         |            | correct          | choice,      |           | 45      |            |
| blank                   | lines,  | 8, 9,     | 14, 15  |            | \checkboxeshook, |              |           | 41      |            |
| blank                   | space,  | 9, 56     |         |            | \checkedchar,    |              | 49        |         |            |
| \boldmath,              |         | 28        |         |            | \choice,         | 13,          | 42–45     |         |            |
| bonus                   | points, | 35–37,    | 95      |            | choice,          | 40           |           |         |            |
| \bonusgradetable,       |         |           | 36,     | 95         | choice           | counter,     | 40        |         |            |
| \bonuspart,             |         | 35,       | 36      |            | \choicelabel,    |              | 40,       | 41      |            |
| \bonuspointformat,      |         |           | 26,     | 27         | choices,         | 13,          | 42,       | 48      |            |
| \bonuspointname,        |         |           | 27, 37  |            | choices          | environment, |           | 42      |            |
| \bonuspointpoints,      |         |           | 25,     | 36, 37     | correct          | choice,      |           | 45      |            |
| \bonuspointsinrange,    |         |           |         | 95         | \choiceshook,    |              | 41        |         |            |
| \bonuspointsofquestion, |         |           |         | 31, 36, 95 | \chpgword,       |              | 100       |         |            |
| \bonuspointsonpage,     |         |           | 36,     | 95         | \chpword,        | 100          |           |         |            |
| \bonuspointtable,       |         |           | 36,     | 95         | \chqword,        | 100          |           |         |            |
| \bonusqformat,          |         |           | 33, 36, | 41         | \chsword,        | 100          |           |         |            |
129

| \chtword, | 100    |         |     |     |     | solutionbox,   |     | 79            |     |     |     |
| --------- | ------ | ------- | --- | --- | --- | -------------- | --- | ------------- | --- | --- | --- |
| clickable | links, | 91, 96, | 97  |     |     | solutionorbox, |     |               | 79  |     |     |
| color,    | 48     |         |     |     |     | solution       |     | environments, |     | 79  |     |
color package, 58, 61, 63, 64, 70, 72, 79 grading table, 98–101
| \colorbox,                 | 70      |              |         |              |        | list                   | parameters, |              | 41–42      |            |     |
| -------------------------- | ------- | ------------ | ------- | ------------ | ------ | ---------------------- | ----------- | ------------ | ---------- | ---------- | --- |
| \colorfillwithdottedlines, |         |              |         | 61           |        | margins,               |             | 102–103      |            |            |     |
| \colorfillwithlines,       |         |              | 58      |              |        | multiple               |             | choice       | questions, | 48–49      |     |
| \colorgrids,               |         | 63           |         |              |        | point                  | table,      | 98–101       |            |            |     |
| \colorsolutionboxes,       |         |              | 79      |              |        | points,                | 22–28       |              |            |            |     |
| \combinedgradetable,       |         |              | 36,     | 96           |        | question               |             | numbers,     | 39–41      |            |     |
| \combinedpointtable,       |         |              | 36,     | 96           |        | solution,              |             | 74–75        |            |            |     |
| \ContinuedQuestion,        |         |              | 113,    | 114, 123     |        | \cvbpword,             | 100         |              |            |            |     |
| reliable                   | only    | in           | headers | and footers, | 113    | \cvpgword,             | 100         |              |            |            |     |
| \CorrectChoice,            |         | 13,          | 45      |              |        | \cvpword,              | 100         |              |            |            |     |
| \correctchoice,            |         | 45           |         |              |        | \cvqword,              | 100         |              |            |            |     |
| \CorrectChoiceEmphasis,    |         |              |         | 13, 48,      | 49, 67 | \cvsword,              | 100         |              |            |            |     |
| \correctchoiceemphasis,    |         |              |         | 49           |        | \cvtword,              | 100         |              |            |            |     |
| cover pages,               | 126–128 |              |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | \definecolor,          |             | 58,          | 61, 63,    | 80         |     |
| counting,                  |         | 127–128      |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | \documentclass,        |             | 6,           | 11         |            |     |
| \covercfoot,               |         | 127          |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | options,               |             | 12, 68,      | 77, 83,    | 93, 94     |     |
| \coverchead,               |         | 127          |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | dotted                 | lined       | space,       | 60–62      |            |     |
| \coverextrafootheight,     |         |              | 127     |              |        |                        |             |              |            |            |     |
| \coverextraheadheight,     |         |              | 127     |              |        | \dottedlinefillheight, |             |              |            | 60         |     |
|                            |         |              |         |              |        | \doublerulesep,        |             | 99,          | 100        |            |     |
| \coverfirstpagefooter,     |         |              | 127     |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | \droppoints,           |             | 20–21        |            |            |     |
| \coverfirstpageheader,     |         |              | 127     |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | \droptotalbonuspoints, |             |              |            | 29, 31, 36 |     |
| \coverfooter,              |         | 127          |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | \droptotalpoints,      |             |              | 29,        | 36, 37     |     |
| \coverheader,              |         | 127          |         |              |        |                        |             |              |            |            |     |
| \coverlfoot,               |         | 127          |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | empty,                 | 103         |              |            |            |     |
| \coverlhead,               |         | 127          |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | empty box,             | 56–58       |              |            |            |     |
| coverpages,                |         | 111, 126–128 |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | \endgradingrange,      |             |              | 91–92,     | 95         |     |
| \coverrfoot,               |         | 127          |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | EnvFullwidth,          |             | 50,          | 52–55,     | 71         |     |
| \coverrhead,               |         | 127          |         |              |        |                        |             |              |            |            |     |
|                            |         |              |         |              |        | EnvFullwidth           |             | environment, |            | 50, 52–55, | 71  |
| \coverrunningfooter,       |         |              | 127     |              |        |                        |             |              |            |            |     |
environment
| \coverrunningheader, |     |       | 127 |     |     |             |     |         |     |     |     |
| -------------------- | --- | ----- | --- | --- | --- | ----------- | --- | ------- | --- | --- | --- |
|                      |     |       |     |     |     | checkboxes, |     | 42,     | 44  |     |     |
| cross references,    |     | 38–39 |     |     |     |             |     |         |     |     |     |
|                      |     |       |     |     |     | correct     |     | choice, | 45  |     |     |
customization
|                       |     |       |        |        |      | choices,          | 42    |         |         |     |     |
| --------------------- | --- | ----- | ------ | ------ | ---- | ----------------- | ----- | ------- | ------- | --- | --- |
| \CorrectChoice,       |     |       | 67     |        |      |                   |       |         |         |     |     |
|                       |     |       |        |        |      | correct           |       | choice, | 45      |     |     |
| \answerline,          |     | 65,   | 67     |        |      |                   |       |         |         |     |     |
|                       |     |       |        |        |      | coverpages,       |       | 111,    | 126–128 |     |     |
| \fillin,              |     | 47–48 |        |        |      |                   |       |         |         |     |     |
|                       |     |       |        |        |      | EnvFullwidth,     |       | 50,     | 52–55,  | 71  |     |
| \fillwithdottedlines, |     |       |        | 60, 61 |      |                   |       |         |         |     |     |
|                       |     |       |        |        |      | EnvUplevel,       |       | 50–52,  | 71      |     |     |
| \fillwithgrid,        |     |       | 63     |        |      |                   |       |         |         |     |     |
|                       |     |       |        |        |      | list,             | 41–42 |         |         |     |     |
| \fillwithlines,       |     |       | 59, 60 |        |      |                   |       |         |         |     |     |
|                       |     |       |        |        |      | oneparcheckboxes, |       |         | 42,     | 44  |     |
| \half,                | 22  |       |        |        |      |                   |       |         |         |     |     |
|                       |     |       |        |        |      | correct           |       | choice, | 45      |     |     |
| \makeemptybox,        |     |       | 79     |        |      |                   |       |         |         |     |     |
|                       |     |       |        |        | Page | 130               |       |         |         |     |     |

|     | oneparchoices,         |     |          | 42, 43 |       |       | on                | cover    | pages, | 127     |               |     |
| --- | ---------------------- | --- | -------- | ------ | ----- | ----- | ----------------- | -------- | ------ | ------- | ------------- | --- |
|     | correct                |     | choice,  | 45     |       |       | on                | or off,  | 103    |         |               |     |
|     | parts,                 | 8,  | 9, 13–15 |        |       |       | rule,             | 110–111  |        |         |               |     |
|     | questions,             |     | 7, 13,   | 14     |       |       | three             | parts,   |        | 107–108 |               |     |
|     | solution,              |     | 68–69    |        |       |       | with              | multiple |        | lines,  | 109           |     |
|     | solutionorbox,         |     |          | 68–69  |       |       | \footer,          | 107–108, |        | 120,    | 122, 123, 125 |     |
|     | solutionordottedlines, |     |          |        |       | 68–69 | \footrule,        |          | 110    |         |               |     |
|     | solutionorgrid,        |     |          | 68–69  |       |       | \framedsolutions, |          |        | 72,     | 73            |     |
|     | solutionorlines,       |     |          |        | 68–69 |       | \fullwidth,       |          | 50,    | 52–55,  | 71            |     |
|     | subparts,              |     | 15       |        |       |       |                   |          |        |         |               |     |
grade table
|             | subsubparts, |              | 15     |     |        |     |                            |     |     |        |            |     |
| ----------- | ------------ | ------------ | ------ | --- | ------ | --- | -------------------------- | --- | --- | ------ | ---------- | --- |
|             |              |              |        |     |        |     | customization,             |     |     | 98–101 |            |     |
|             | TheSolution, |              | 75     |     |        |     |                            |     |     |        |            |     |
|             |              |              |        |     |        |     | \gradetable,               |     | 36, | 37,    | 55, 82–101 |     |
| EnvUplevel, |              |              | 50–52, | 71  |        |     |                            |     |     |        |            |     |
| EnvUplevel  |              | environment, |        |     | 50–52, | 71  | \gradetable[h],            |     |     | 83     |            |     |
|             |              |              |        |     |        |     | \gradetable[h][pages],     |     |     |        | 83         |     |
| equation    |              | counter,     |        | 80  |        |     |                            |     |     |        |            |     |
|             |              |              |        |     |        |     | \gradetable[h][questions], |     |     |        | 83         |     |
even pages
|                   |           |     |           |            |         |               | \gradetable[v],            |          |        | 83     |                 |     |
| ----------------- | --------- | --- | --------- | ---------- | ------- | ------------- | -------------------------- | -------- | ------ | ------ | --------------- | --- |
|                   | different |     | from      | odd pages, | 112–113 |               |                            |          |        |        |                 |     |
|                   |           |     |           |            |         |               | \gradetable[v][pages],     |          |        |        | 83              |     |
| \extrafootheight, |           |     |           | 102,       | 109     |               |                            |          |        |        |                 |     |
|                   |           |     |           |            |         |               | \gradetable[v][questions], |          |        |        | 83              |     |
|                   | different |     | on first  | page,      | 109     |               |                            |          |        |        |                 |     |
|                   |           |     |           |            |         |               | \gradetablestretch,        |          |        |        | 99, 100         |     |
|                   | optional  |     | argument, |            | 103     |               |                            |          |        |        |                 |     |
|                   |           |     |           |            |         |               | grading                    | range,   | 91–92  |        |                 |     |
| \extraheadheight, |           |     |           | 102,       | 108,    | 109, 120, 122 |                            |          |        |        |                 |     |
|                   |           |     |           |            |         |               | grading                    | table,   | 82–101 |        |                 |     |
|                   | different |     | on first  | page,      | 109     |               |                            |          |        |        |                 |     |
|                   | optional  |     | argument, |            | 102     |               | bonus,                     |          | 95–96  |        |                 |     |
|                   |           |     |           |            |         |               | by                         | question |        | number | or page number, | 82– |
| \extrawidth,      |           |     | 26,       | 31, 102    |         |               |                            |          |        |        |                 |     |
85
| \fbox,                    |        | 70, 72 |        |        |          |          | changing       |        | total  | points, | 98  |     |
| ------------------------- | ------ | ------ | ------ | ------ | -------- | -------- | -------------- | ------ | ------ | ------- | --- | --- |
| fill                      | in the | blank, | 45–48  |        |          |          | clickable      |        | links, | 91      |     |     |
| \fillin,                  |        | 45–48  |        |        |          |          | combined,      |        | 96–97  |         |     |     |
| \fillinlinelength,        |        |        |        | 47     |          |          | graph          | paper, | 65     |         |     |     |
| \fillwithdottedlines,     |        |        |        |        | 60–62,   | 69, 76   | graphics,      | 73     |        |         |     |     |
| FillWithDottedLinesColor, |        |        |        |        |          | 61       | \greeknum,     |        | 40     |         |     |     |
| \fillwithgrid,            |        |        | 62–65, |        | 69, 76   |          | grid           |        |        |         |     |     |
| \fillwithlines,           |        |        |        | 58–60, | 69, 75   |          | covering       |        | every  | page,   | 64  |     |
| FillWithLinesColor,       |        |        |        |        | 58       |          | grid space,    |        | 62–65  |         |     |     |
| \firstpagefooter,         |        |        |        | 10,    | 107–108, | 118, 119 | GridColor,     |        | 63     |         |     |     |
| \firstpagefootrule,       |        |        |        |        | 10, 110  |          | \gridfromfoot, |        |        | 64      |     |     |
\firstpageheader,10,104–105,117–120,122–
\half, 22
125
|                     |     |     |     |     |         |     | customization, |     |     | 22  |     |     |
| ------------------- | --- | --- | --- | --- | ------- | --- | -------------- | --- | --- | --- | --- | --- |
| \firstpageheadrule, |     |     |     |     | 10, 110 |     |                |     |     |     |     |     |
|                     |     |     |     |     |         |     | half points,   |     | 22  |     |     |     |
| \firstqinrange,     |     |     |     | 91  |         |     |                |     |     |     |     |     |
head, 103
foot, 103
| foot    | height |        |            |     |     |      | head height  |      |            |     |     |     |
| ------- | ------ | ------ | ---------- | --- | --- | ---- | ------------ | ---- | ---------- | --- | --- | --- |
|         |        |        |            |     |     |      | first        | page | different, |     | 102 |     |
|         | first  | page   | different, |     | 103 |      |              |      |            |     |     |     |
|         |        |        |            |     |     |      | headandfoot, |      | 103        |     |     |     |
| footer, |        | 10–11, | 103–126    |     |     |      |              |      |            |     |     |     |
|         |        |        |            |     |     | Page | 131          |      |            |     |     |     |

| header,    | 10–11,   | 103–126  |        |          |     | \linefillthickness,    |             |         | 60     |            |        |
| ---------- | -------- | -------- | ------ | -------- | --- | ---------------------- | ----------- | ------- | ------ | ---------- | ------ |
| different  |          | on first | page,  | 104, 105 |     | list environment,      |             |         | 41–42  |            |        |
| multiple   |          | lines,   | 106,   | 107      |     | LPPL,                  | 6           |         |        |            |        |
| on         | cover    | pages,   | 127    |          |     |                        |             |         |        |            |        |
| on         | or off,  | 103      |        |          |     | \makeemptybox,         |             |         | 56–58, | 69, 75     |        |
|            |          |          |        |          |     | \maketitle,            |             | 104     |        |            |        |
| rule,      | 110–111  |          |        |          |     |                        |             |         |        |            |        |
|            |          |          |        |          |     |                        | overriding, | 104     |        |            |        |
| three      | parts,   | 104–106  |        |          |     |                        |             |         |        |            |        |
|            |          |          |        |          |     | \marginbonuspointname, |             |         |        | 27, 29,    | 37     |
| with       | multiple |          | lines, | 108–109  |     |                        |             |         |        |            |        |
|            |          |          |        |          |     | \marginpointname,      |             |         | 19,    | 20, 25–27, | 29, 38 |
| \header,   | 104–105  |          |        |          |     |                        |             |         |        |            |        |
|            |          |          |        |          |     | \marginpointssep,      |             |         | 31     |            |        |
| \headrule, |          | 110      |        |          |     |                        |             |         |        |            |        |
|            |          |          |        |          |     | margins,               | 4,          | 102–103 |        |            |        |
| \hpgword,  | 99       |          |        |          |     |                        |             |         |        |            |        |
|            |          |          |        |          |     |                        | enlarge,    | 26,     | 31     |            |        |
| \hpword,   | 99       |          |        |          |     |                        |             |         |        |            |        |
marks, 25
| \hqword,  | 99  |     |     |     |     |                                 |     |     |       |     |     |
| --------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | ----- | --- | --- |
| \hsword,  | 99  |     |     |     |     | \marksnotpoints,                |     |     | 8, 25 |     |     |
|           |     |     |     |     |     | \multicolumnbonusgradetable,    |     |     |       |     | 95  |
| \htword,  | 99  |     |     |     |     |                                 |     |     |       |     |     |
|           |     |     |     |     |     | \multicolumnbonuspointtable,    |     |     |       |     | 95  |
| hyperref, | 91, | 95, | 97  |     |     |                                 |     |     |       |     |     |
|           |     |     |     |     |     | \multicolumncombinedgradetable, |     |     |       |     | 96  |
\ifcontinuation,55,113,114,116,123,125 \multicolumncombinedpointtable, 96
reliable only in headers and footers, 113 \multicolumngradetable, 86
\ifincomplete, 55, 113, 115–116, 123 \multicolumnpartialbonusgradetable, 95
reliable only in headers and footers, 113 \multicolumnpartialbonuspointtable, 95
\iflastpage, 111–113, 115, 120 \multicolumnpartialcombinedgradetable,
| \ifprintanswers, |     |     | 80–82 |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
96
| \includegraphics,    |     |     | 73  |                |     | \multicolumnpartialcombinedpointtable, |     |     |     |     |     |
| -------------------- | --- | --- | --- | -------------- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
| \IncompleteQuestion, |     |     |     | 113, 115, 123, | 125 |                                        | 96  |     |     |     |     |
reliable only in headers and footers, 113 \multicolumnpartialgradetable, 93
| indentation,   |          | 50–55     |          |     |     | \multicolumnpartialpointtable,      |         |     |     |     | 93  |
| -------------- | -------- | --------- | -------- | --- | --- | ----------------------------------- | ------- | --- | --- | --- | --- |
| remove,        |          | 33, 41    |          |     |     | \multicolumnpointtable,             |         |     |     | 90  |     |
| instructions,  |          | 50–53     |          |     |     | multiple                            | choice, |     | 42  |     |     |
| \itemsep,      | 41       |           |          |     |     | \multirowbonusgradetable,           |         |     |     | 95  |     |
|                |          |           |          |     |     | \multirowbonuspointtable,           |         |     |     | 95  |     |
| kerning,       | 41       |           |          |     |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowcombinedgradetable,        |         |     |     |     | 96  |
|                |          |           |          |     |     | \multirowcombinedpointtable,        |         |     |     |     | 96  |
| \labelsep,     |          | 41        |          |     |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowgradetable,                |         |     |     | 85  |     |
| last page,     | 111–112  |           |          |     |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowpartialbonusgradetable,    |         |     |     |     | 95  |
| \lastqinrange, |          |           | 91       |     |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowpartialbonuspointtable,    |         |     |     |     | 95  |
| LATEX          | Project  | Public    | License, | 6   |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowpartialcombinedgradetable, |         |     |     |     | 96  |
| \leftmargin,   |          | 41        |          |     |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowpartialcombinedpointtable, |         |     |     |     | 96  |
| \lfoot,        | 108,     | 117–126   |          |     |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowpartialgradetable,         |         |     |     |     | 92  |
| \lhead,        | 105–106, |           | 117–126  |     |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowpartialpointtable,         |         |     |     |     | 92  |
| different      |          | on first  | page,    | 105 |     |                                     |         |     |     |     |     |
|                |          |           |          |     |     | \multirowpointtable,                |         |     |     | 89  |     |
| optional       |          | argument, |          | 105 |     |                                     |         |     |     |     |     |
| license,       | 6        |           |          |     |     |                                     |         |     |     |     |     |
name, 6
| lined space,     |     | 58–60 |     |     |      |        |       |     |           |       |     |
| ---------------- | --- | ----- | --- | --- | ---- | ------ | ----- | --- | --------- | ----- | --- |
|                  |     |       |     |     |      | naming | parts | of  | the exam, | 53–55 |     |
| \linefillheight, |     |       | 60  |     |      |        |       |     |           |       |     |
|                  |     |       |     |     | Page | 132    |       |     |           |       |     |

| \newpage,                   | 56,   | 58     |         |     | \parsep,                    |                | 41         |         |          |      |         |     |
| --------------------------- | ----- | ------ | ------- | --- | --------------------------- | -------------- | ---------- | ------- | -------- | ---- | ------- | --- |
| \noaddpoints,               |       | 12,    | 38      |     | \part,                      | 8,             | 13         |         |          |      |         |     |
| \nobonusqformat,            |       |        | 36      |     |                             | optional       | argument,  |         | 18       |      |         |     |
| \noboxedpoints,             |       | 23,    | 24      |     |                             | standard       | sectioning |         | command, |      | 53,     | 55  |
| \nobracketedpoints,         |       |        | 23      |     | part                        | counter,       | 40         |         |          |      |         |     |
| \nocancelspace,             |       | 77–78  |         |     | \partialbonusgradetable,    |                |            |         |          | 95   |         |     |
| \nocolorsolutionboxes,      |       |        |         | 80  | \partialbonuspointtable,    |                |            |         |          | 95   |         |     |
| \nomorequestions,           |       |        | 114,    | 116 | \partialcombinedgradetable, |                |            |         |          |      | 96      |     |
| \nopointsinmargin,          |       |        | 18,     | 24  | \partialcombinedpointtable, |                |            |         |          |      | 96      |     |
| \nopointsinrightmargin,     |       |        |         | 18  | \partialgradetable,         |                |            |         | 92       |      |         |     |
| \noprintanswers,            |       |        | 68      |     | \partialpointtable,         |                |            |         | 92       |      |         |     |
| \noqformat,                 |       | 32, 36 |         |     | \partlabel,                 |                | 40         |         |          |      |         |     |
| \noquestionsonthispage,     |       |        |         | 116 | partno,                     | 40             |            |         |          |      |         |     |
| \nosolutionsreseteqcounter, |       |        |         | 80  | \partopsep,                 |                | 41         |         |          |      |         |     |
| \nounstarredvspace,         |       |        | 69      |     | parts,                      | 8,             | 9, 13–15   |         |          |      |         |     |
| \numbonuspoints,            |       |        | 36, 37  |     | parts                       | environment,   |            | 8,      | 9, 13–15 |      |         |     |
| \numcoverpages,             |       | 111,   | 127–128 |     | \partshook,                 |                | 41         |         |          |      |         |     |
| \numpages,                  | 111,  | 120,   | 123–125 |     | point                       | table,         | 82–101     |         |          |      |         |     |
| doesn’t                     | count | cover  | pages,  | 111 |                             | bonus,         | 95–96      |         |          |      |         |     |
| \numparts,                  | 37    |        |         |     |                             | by question    |            | number  | or       | page | number, | 87– |
| \numpoints,                 |       | 36, 37 |         |     |                             | 89             |            |         |          |      |         |     |
| \numqinrange,               |       | 91     |         |     |                             | changing       | total      | points, |          | 98   |         |     |
| \numquestions,              |       | 37     |         |     |                             | clickable      | links,     | 91      |          |      |         |     |
| \numsubparts,               |       | 37     |         |     |                             | combined,      | 96–97      |         |          |      |         |     |
| \numsubsubparts,            |       |        | 37      |     |                             | customization, |            | 98–101  |          |      |         |     |
|                             |       |        |         |     | \pointformat,               |                |            | 26–28   |          |      |         |     |
odd pages
|                   |            |      |        |                    | \pointname,   |            | 24,       | 25,      | 27, 32, | 38  |     |     |
| ----------------- | ---------- | ---- | ------ | ------------------ | ------------- | ---------- | --------- | -------- | ------- | --- | --- | --- |
| different         | from       | even | pages, | 112–113            |               |            |           |          |         |     |     |     |
|                   |            |      |        |                    | \pointpoints, |            |           | 24, 25,  | 32      |     |     |     |
| \oddeven,         | 112,       | 125  |        |                    |               |            |           |          |         |     |     |     |
|                   |            |      |        |                    | points,       | 5,         | 13, 18–31 |          |         |     |     |     |
| only              | in headers |      | and    | footers, 113       |               |            |           |          |         |     |     |     |
|                   |            |      |        |                    |               | acceptable |           | entries, | 38      |     |     |     |
| oneparcheckboxes, |            |      | 13,    | 42, 44, 45, 48, 49 |               |            |           |          |         |     |     |     |
|                   |            |      |        |                    |               | adding,    | 33        |          |         |     |     |     |
oneparcheckboxes environment, 42, 44 at the end of the question, 20–21
| correct                  | choice,    | 45           |     |            |                        |                |          |       |       |         |     |     |
| ------------------------ | ---------- | ------------ | --- | ---------- | ---------------------- | -------------- | -------- | ----- | ----- | ------- | --- | --- |
|                          |            |              |     |            |                        | bonus,         | 35–37,   | 95    |       |         |     |     |
| oneparchoices,           |            | 13,          | 42, | 43, 45, 48 |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            |                        | customization, |          | 22–28 |       |         |     |     |
| oneparchoices            |            | environment, |     | 42, 43     |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            |                        | for both       | question |       | and   | part,   | 28  |     |
| correct                  | choice,    | 45           |     |            |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            |                        | half, 22       |          |       |       |         |     |     |
| optional                 | arguments, |              | 107 |            |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            |                        | language,      | 24–28    |       |       |         |     |     |
|                          |            |              |     |            |                        | substitute     | words,   |       | 24–28 |         |     |     |
| \pagestyle,              |            | 10, 103–104  |     |            |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            |                        | total,         | 5        |       |       |         |     |     |
| default,                 | 104        |              |     |            |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            |                        | where          | printed, | 18–21 |       |         |     |     |
| \pagestyle{empty},       |            |              | 103 |            |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            | \points,               |                | 24, 32   |       |       |         |     |     |
| \pagestyle{foot},        |            |              | 103 |            |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            | \pointsdroppedatright, |                |          |       |       | 20–21,  | 30  |     |
| \pagestyle{head},        |            |              | 103 |            |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            | \pointsinleftmargin,   |                |          |       | 18,   | 19      |     |     |
| \pagestyle{headandfoot}, |            |              |     | 103        |                        |                |          |       |       |         |     |     |
|                          |            |              |     |            | \pointsinmargin,       |                |          | 18,   | 19,   | 23, 25, | 27, | 31  |
Page 133

| \pointsinrange,       |     |     | 91  |            |         | \romannumeral, |           |     | 127     |         |     |
| --------------------- | --- | --- | --- | ---------- | ------- | -------------- | --------- | --- | ------- | ------- | --- |
| \pointsinrightmargin, |     |     |     | 18–20, 23, | 25, 27, | rule           |           |     |         |         |     |
|                       | 31  |     |     |            |         |                | in header | or  | footer, | 110–111 |     |
\pointsofquestion, 30, 32, 36, 93–95 \runningfooter, 10, 107–108, 118, 119, 124
\pointsonpage, 36, 94, 95, 124 \runningfootrule, 10, 110, 118
|                  | in footer, | 94  |     |     |     | \runningheader, |     |     | 10, 104–105, | 117–120, | 122– |
| ---------------- | ---------- | --- | --- | --- | --- | --------------- | --- | --- | ------------ | -------- | ---- |
| \pointstwosided, |            |     | 18  |     |     |                 | 125 |     |              |          |      |
\pointstwosidedreversed, 18 \runningheadrule, 10, 110, 117, 123
| \pointtable,               |     | 36,    | 37, | 55, 82–101 |     |                            |           |           |     |     |     |
| -------------------------- | --- | ------ | --- | ---------- | --- | -------------------------- | --------- | --------- | --- | --- | --- |
|                            |     |        |     |            |     | \section,                  |           | 53, 55    |     |     |     |
| \pointtable[h],            |     |        | 87  |            |     |                            |           |           |     |     |     |
|                            |     |        |     |            |     | selected                   | solution, |           | 81  |     |     |
| \pointtable[h][pages],     |     |        |     | 87         |     |                            |           |           |     |     |     |
|                            |     |        |     |            |     | \settabletotalbonuspoints, |           |           |     | 98  |     |
| \pointtable[h][questions], |     |        |     | 87         |     |                            |           |           |     |     |     |
|                            |     |        |     |            |     | \settabletotalpoints,      |           |           |     | 98  |     |
| \pointtable[v],            |     |        | 87  |            |     |                            |           |           |     |     |     |
| \pointtable[v][pages],     |     |        |     | 87         |     | \shadedsolutions,          |           |           | 70, | 72  |     |
|                            |     |        |     |            |     | short                      | answers,  | 65–68     |     |     |     |
| \pointtable[v][questions], |     |        |     | 87         |     |                            |           |           |     |     |     |
|                            |     |        |     |            |     |                            | answers   | to, 67–68 |     |     |     |
| preamble,                  |     | 48, 49 |     |            |     |                            |           |           |     |     |     |
solution
| \printanswers,  |                |            | 13, 45, | 68, 71 |     |                   |              |              |          |           |     |
| --------------- | -------------- | ---------- | ------- | ------ | --- | ----------------- | ------------ | ------------ | -------- | --------- | --- |
|                 |                |            |         |        |     |                   | appearance,  | 70–75        |          |           |     |
| \qformat,       |                | 20, 32–36, |         | 41     |     |                   | customizing, |              | 74–75    |           |     |
| \question,      |                | 7, 13,     | 14,     | 34, 35 |     |                   | in a box,    | 70–72,       | 78       |           |     |
|                 | optional       | argument,  |         | 18     |     |                   | no framing   | or           | shading, | 72–73     |     |
| question,       |                | 40         |         |        |     |                   | selected,    | 81           |          |           |     |
| question        | counter,       |            | 40      |        |     |                   | shaded,      | 72           |          |           |     |
| question        | number,        |            | 34, 35  |        |     | solution          |              | environment, |          | 13, 68–82 |     |
| \questionlabel, |                |            | 40      |        |     |                   | optional     | argument,    |          | 69, 75–78 |     |
| questions       |                |            |         |        |     | solutionbox,      |              | 13,          | 78       |           |     |
|                 | counting,      | 37–38      |         |        |     | SolutionBoxColor, |              |              | 80       |           |     |
|                 | customization, |            | 32–33   |        |     | \SolutionColor,   |              |              | 72       |           |     |
that begin with a parts environment, 28 \SolutionEmphasis, 73–75
|            | that span | multiple |     | pages, 113–116 |     | solutionorbox, |          |           | 13  |     |     |
| ---------- | --------- | -------- | --- | -------------- | --- | -------------- | -------- | --------- | --- | --- | --- |
| questions, |           | 7, 13,   | 14  |                |     |                | optional | argument, |     | 75  |     |
questions environment, 7, 13, 14 solutionorbox environment, 68–69
|                 | only one, | 83  |     |     |     | solutionordottedlines, |          |           |              | 13  |       |
| --------------- | --------- | --- | --- | --- | --- | ---------------------- | -------- | --------- | ------------ | --- | ----- |
| \questionshook, |           |     | 41  |     |     |                        | optional | argument, |              | 76  |       |
|                 |           |     |     |     |     | solutionordottedlines  |          |           | environment, |     | 68–69 |
range
|                     |           |           |             |        |     | solutionorgrid,           |          |              | 13  |       |     |
| ------------------- | --------- | --------- | ----------- | ------ | --- | ------------------------- | -------- | ------------ | --- | ----- | --- |
|                     | grading,  | 91–92     |             |        |     |                           |          |              |     |       |     |
|                     |           |           |             |        |     |                           | optional | argument,    |     | 76    |     |
| \rfoot,             | 108,      | 117–126   |             |        |     |                           |          |              |     |       |     |
|                     |           |           |             |        |     | solutionorlines,          |          |              | 13  |       |     |
| \rhead,             | 105–106,  |           | 117–126     |        |     |                           |          |              |     |       |     |
|                     |           |           |             |        |     |                           | optional | argument,    |     | 75    |     |
|                     | different | on        | first page, | 105    |     |                           |          |              |     |       |     |
|                     |           |           |             |        |     | solutionorlines           |          | environment, |     | 68–69 |     |
|                     | optional  | argument, |             | 105    |     |                           |          |              |     |       |     |
|                     |           |           |             |        |     | solutions,                |          | 45, 68–82    |     |       |     |
| \rightpointsmargin, |           |           |             | 30, 31 |     | \solutionsreseteqcounter, |          |              |     | 80    |     |
| \Roman,             | 40        |           |             |        |     |                           |          |              |     |       |     |
|                     |           |           |             |        |     | \solutiontitle,           |          |              | 74  |       |     |
| \roman,             | 40        |           |             |        |     |                           |          |              |     |       |     |
space
|     |     |     |     |     | Page | 134 |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |

| allocating,       |              | 10,          | 56, 58, | 60, 62, 64 |     | \totalformat,          |            | 29–31 |              |
| ----------------- | ------------ | ------------ | ------- | ---------- | --- | ---------------------- | ---------- | ----- | ------------ |
| blank,            | 9,           | 56           |         |            |     | \totalnumpages,        |            |       | 111, 127–128 |
| dotted            | lined,       | 60–62        |         |            |     | \totalpoints,          |            | 30–33 |              |
| empty             | box,         | 56–58        |         |            |     | true/false             | questions, |       | 47           |
| for               | answers,     | 9,           | 55–68,  | 75–79      |     |                        |            |       |              |
|                   |              |              |         |            |     | \unframedsolutions,    |            |       | 72, 75       |
| grid,             | 62–65        |              |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \unstarredvspace,      |            |       | 69, 75       |
| lined,            | 58–60        |              |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \uplevel,              | 50–55,     |       | 71           |
| \stretch,         | 10,          | 56,          | 58, 60, | 62, 64     |     |                        |            |       |              |
|                   |              |              |         |            |     | \usehorizontalhalf,    |            |       | 22           |
| student’s         | name,        | 6            |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \usepackage{hyperref}, |            |       | 91, 95, 97   |
| \subpart,         | 15           |              |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \useslantedhalf,       |            |       | 22           |
| optional          |              | argument,    | 18      |            |     |                        |            |       |              |
|                   |              |              |         |            |     | Utopia                 | font,      | 40    |              |
| subpart,          | 40           |              |         |            |     |                        |            |       |              |
| subpart           | counter,     | 40           |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \vpgword,              | 99         |       |              |
| \subpartlabel,    |              | 40           |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \vpword,               | 99         |       |              |
| subparts,         | 15           |              |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \vqword,               | 99         |       |              |
| subparts          | environment, |              | 15      |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \vspace,               | 56,        | 69,   | 75           |
| \subpartshook,    |              | 41           |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \vspace*,              | 56,        | 69,   | 75           |
| \subsubpart,      |              | 15           |         |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \vsword,               | 99         |       |              |
| optional          |              | argument,    | 18      |            |     |                        |            |       |              |
|                   |              |              |         |            |     | \vtword,               | 99         |       |              |
| subsubpart,       |              | 40           |         |            |     |                        |            |       |              |
| subsubpart        | counter,     |              | 40      |            |     | web page,              | 6          |       |              |
| \subsubpartlabel, |              |              | 40      |            |     |                        |            |       |              |
| subsubparts,      |              | 15           |         |            |     | xcolor,                | see color  |       |              |
| subsubparts       |              | environment, |         | 15         |     |                        |            |       |              |
| \subsubpartshook, |              |              | 41      |            |     |                        |            |       |              |
\surd, 49
| \thechoice,                  |      | 39           |         |              |     |     |     |     |     |
| ---------------------------- | ---- | ------------ | ------- | ------------ | --- | --- | --- | --- | --- |
| \themarginpoints,            |      |              | 27      |              |     |     |     |     |     |
| \thepage,                    | 120, | 123–125      |         |              |     |     |     |     |     |
| reliable                     | only | in           | headers | and footers, | 94  |     |     |     |     |
| \thepartno,                  |      | 39, 40       |         |              |     |     |     |     |     |
| \thepoints,                  |      | 26, 27,      | 32,     | 33, 36       |     |     |     |     |     |
| \thequestion,                |      | 30–34,       | 39,     | 40           |     |     |     |     |     |
| \thequestiontitle,           |      |              | 32,     | 34, 35       |     |     |     |     |     |
| TheSolution,                 |      | 75           |         |              |     |     |     |     |     |
| TheSolution                  |      | environment, |         | 75           |     |     |     |     |     |
| \thesubpart,                 |      | 39           |         |              |     |     |     |     |     |
| \thesubsubpart,              |      |              | 39      |              |     |     |     |     |     |
| \thispagestyle,              |      |              | 104     |              |     |     |     |     |     |
| \thispagestyle{headandfoot}, |      |              |         | 104          |     |     |     |     |     |
| \titledquestion,             |      |              | 32, 34, | 35           |     |     |     |     |     |
| \topsep,                     | 41   |              |         |              |     |     |     |     |     |
| \totalbonuspoints,           |      |              | 31,     | 37           |     |     |     |     |     |
Page 135
