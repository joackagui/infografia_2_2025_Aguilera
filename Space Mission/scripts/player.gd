extends CharacterBody2D

# PROPERTIES
@export var speed: float = 200.0
@export var jump_velocity: float = -400.0
@export var hp: int = 50

signal player_hurt

var gravity: float = ProjectSettings.get_setting("physics/2d/default_gravity")
@onready var state_machine = $AnimationTree.get("parameters/playback")

enum {
	WALK,
	DUCK,
	JUMP,
	IDLE
}

var state = IDLE

func _physics_process(delta: float) -> void:
	if not is_on_floor():
		velocity.y += gravity * delta
		if state != JUMP:
			state_machine.travel("Jump")
		
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		state = JUMP
		velocity.y = jump_velocity
		state_machine.travel("Jump")
		
	if Input.is_action_pressed("ui_down") and is_on_floor():
		state = DUCK
		state_machine.travel("Duck")
		velocity.x = 0
	else:
		var direction = Input.get_axis("ui_left", "ui_right")
		if direction:
			velocity.x = direction * speed
			if is_on_floor():
				state_machine.travel("Walk")
				state = WALK
			
			$Sprite2D.scale.x = abs($Sprite2D.scale.x) * sign(direction)
		else:
			velocity.x = move_toward(velocity.x, 0, speed)
			if is_on_floor():
				state = IDLE
				state_machine.travel("Idle")

	move_and_slide()

func _on_hurtbox_area_entered(area: Area2D) -> void:
	hp -= 10
	player_hurt.emit()
	if hp <= 0:
		queue_free()
