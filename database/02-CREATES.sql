create table IF NOT EXISTS app_poker.game (
    game_cd_game uuid primary key,
    game_tx_opponent_email text not null,
    game_li_first_hand TEXT[] not null,
    game_li_second_hand TEXT[],
    game_li_changes TEXT[],
    game_in_finished bool,
    game_tx_result text,
    game_nr_first_bet int,
    game_nr_second_bet int,
    game_nr_pot int,
    game_nr_balance int
);


comment on table app_poker.game is 'Table to store the game matches data';
comment on column app_poker.game.game_cd_game is 'Game id';
comment on column app_poker.game.game_tx_opponent_email is 'Opponent email';
comment on column app_poker.game.game_li_first_hand is 'First hand cards';
comment on column app_poker.game.game_li_second_hand is 'Second hand cards';
comment on column app_poker.game.game_li_changes is 'Changes made in the hand';
comment on column app_poker.game.game_in_finished is 'Game finished';
comment on column app_poker.game.game_tx_result is 'Game result';
comment on column app_poker.game.game_nr_first_bet is 'First bet';
comment on column app_poker.game.game_nr_second_bet is 'Second bet';
comment on column app_poker.game.game_nr_pot is 'Sum of first and second bet called as Pot';
comment on column app_poker.game.game_nr_balance is 'Balance of the game';
