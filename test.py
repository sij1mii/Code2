import ui
import sound

def tapped_button(sender):
	#a = sound.load_effect('Explosion_1')
	sound.play_effect('Jump')
	#sound.play_effect('Explosion_1')
def tapped_button(sender):
	sound.play_effect('Explosion_1')

v = ui.load_view()
v.present('sheet')
