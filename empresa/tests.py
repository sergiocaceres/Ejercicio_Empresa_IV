from django.test import TestCase

class Test(TestCase):
	def test_form(self):
		c = Post(nombre_empresa = 'EmpresaTest', persona = 'PersonaTest', fecha = timezone.now(), puntuacion = '9')
		c.save()
		self.assertEqual(c.nombre_empresa, "EmpresaTest")
