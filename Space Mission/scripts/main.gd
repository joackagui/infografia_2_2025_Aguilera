extends Node2D

@onready var door: Area2D = $Door
@onready var enemyA: Node2D = $EnemyA
@onready var hp_label: Label = $HpLabel
@onready var score_label: Label = $ScoreLabel

var score: int = 0

func _ready() -> void:
	$Key.key_collected.connect(on_key_collected)
	$Player.player_hurt.connect(on_player_hurt)
	$Gem.gem_collected.connect(on_gem_colected)
	$Door.win.connect(on_finish)
	update_hp_label()
	update_score()
	get_tree().paused = false
	
func on_finish():
	get_tree().paused = true
	hp_label.text = "Winner"

func on_gem_colected():
	enemyA.death()
	update_score()

func on_key_collected():
	door.open()
	update_score()

func on_player_hurt():
	update_hp_label()

func update_hp_label():
	hp_label.text = "Player HP: " + str($Player.hp)
	
func update_score():
	score += 100
	score_label.text = "Score: " + str(score)
