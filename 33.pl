
vowel_count([], 0).

vowel_count([H|T], Count) :-
    vowel(H),
    vowel_count(T, TailCount),
    Count is TailCount + 1.

vowel_count([H|T], Count) :-
    \+ vowel(H),
    vowel_count(T, Count).

% Define vowels
vowel(a).
vowel(e).
vowel(i).
vowel(o).
vowel(u).
vowel(A) :- char_code(A, Code), Code >= 65, Code =< 90, char_code(Lower, Code + 32), vowel(Lower). % handles uppercase vowels

