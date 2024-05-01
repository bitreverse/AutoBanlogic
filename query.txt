A registers his ID and secret information, K<sub>ab</sub> with B in advance.

<Messages>
Message 1: A → B: (ID<sub>A</sub>, Q<sub>A</sub>)
Message 2: B → A: (ID<sub>B</sub>, Q<sub>B</sub>, HMAC(K<sub>ab</sub>, (Q<sub>A</sub>, Q<sub>B</sub>)))
Message 3: A → B: HMAC(K<sub>ab</sub>, (Q<sub>B</sub>, Q<sub>A</sub>))

<Assumptions>
(A1) A believes A⇐<sup>K<sub>ab</sub></sup>⇒B
(A2) A believes fresh(Q<sub>A</sub>)
(A3) B believes A⇐<sup>K<sub>ab</sub></sup>⇒B
(A4) B believes fresh(Q<sub>B</sub>)

<Goals>
(G1) A believes B believes (<Q<sub>A</sub>, <Q<sub>B</sub>) 
(G2) B believes A believes (<Q<sub>B</sub>, <Q<sub>A</sub>)