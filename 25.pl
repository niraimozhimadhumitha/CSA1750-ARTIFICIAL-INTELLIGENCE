

initial(state(at_floor, at_floor, at_ceiling)).

action(state(at_ceiling, at_floor, at_ceiling), monkey_grab, state(at_ceiling, at_floor, at_ceiling)).
action(state(on_box, at_floor, at_ceiling), monkey_grab, state(on_box, at_floor, at_floor)).
action(state(at_floor, at_floor, at_ceiling), monkey_climb, state(on_box, at_floor, at_ceiling)).
action(state(at_floor, at_floor, at_ceiling), monkey_push, state(at_floor, on_box, at_ceiling)).

goal(state(_, _, at_floor)).

solve(State, Path) :-
    goal(State),                  
    Path = [].                   
solve(State, [Action|Rest]) :-
    action(State, Action, NextState),  
    solve(NextState, Rest).           

