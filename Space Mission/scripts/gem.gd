extends Area2D

signal gem_collected

func _on_body_entered(body: Node2D) -> void:
	gem_collected.emit()
	queue_free()
