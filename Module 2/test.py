def saluda(self):
    print('Hola, soy un método!')

User = type('User', (object, ), {
    'saluda': saluda
})

eduardo = User()
eduardo.saluda()