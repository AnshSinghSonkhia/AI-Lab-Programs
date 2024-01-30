% Rules for solving the water jug problem

% Initial state
initial_state(0, 0).

% Goal state
goal_state(4, _).

% Actions to be taken
% Filling a jug completely
fill(A, _, A).

fill(_, B, B).

% Emptying a jug completely
empty(A, _, 0).

empty(_, B, 0).

% Pouring water from one jug to another
pour(A, B, A1, B1) :-
    A > 0, B < 3, A1 is max(A - (3 - B), 0), B1 is min(B + A, 3).

pour(A, B, A1, B1) :-
    A < 4, B > 0, B1 is max(B - (4 - A), 0), A1 is min(A + B, 4).

% Define the solution
solve(State, State, Actions, Actions).

solve(CurrentState, GoalState, Actions, AllActions) :-
    pour(CurrentA, CurrentB, NewA, NewB),
    NewState = (NewA, NewB),
    \+ member(NewState, Actions),  % To avoid revisiting the same state
    solve(NewState, GoalState, [NewState | Actions], AllActions).

% Entry point to find a solution
find_solution(Actions) :-
    initial_state(InitialA, InitialB),
    goal_state(GoalA, GoalB),
    solve((InitialA, InitialB), (GoalA, GoalB), [(InitialA, InitialB)], Actions).

% Example query to find a solution
% ?- find_solution(Actions).
