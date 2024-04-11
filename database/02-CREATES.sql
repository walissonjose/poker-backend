create table IF NOT EXISTS app_poker.game (
    game_cd_game uuid primary key,
    game_tx_opponent_email text not null,
    game_li_hand TEXT[] not null,
    game_tx_result text,
    game_nr_first_bet int,
    game_nr_opponent_first_bet int,
    game_nr_pot int,
    game_nr_balance int
);


comment on table app_poker.game is 'Table to store the game matches data';
comment on column app_poker.game.game_cd_game is 'Game id';
comment on column app_poker.game.game_tx_opponent_email is 'Opponent email';
comment on column app_poker.game.game_li_hand is 'Hand cards';
comment on column app_poker.game.game_tx_result is 'Game result';
comment on column app_poker.game.game_nr_first_bet is 'First bet';
comment on column app_poker.game.game_nr_opponent_first_bet is 'Opponent first bet';
comment on column app_poker.game.game_nr_balance is 'Balance of the game';
