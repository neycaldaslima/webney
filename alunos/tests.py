from django.test import TestCase
from django.urls import reverse

from .models import Aluno


class CadastrarAlunoTests(TestCase):
    def test_duplicate_matricula_shows_error_without_saving(self):
        Aluno.objects.create(
            cpf='12345678901',
            matricula='2026001',
            nome='Ana Silva',
            idade=20,
            email='ana@example.com',
            telefone='11999999999',
            endereco='Rua A',
        )

        response = self.client.post(
            reverse('cadastrar_alunos'),
            {
                'cpf': '10987654321',
                'matricula': '2026001',
                'nome': 'Bruno Lima',
                'idade': '',
                'email': 'bruno@example.com',
                'telefone': '11888888888',
                'endereco': 'Rua B',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Esta matrícula já está cadastrada.')
        self.assertEqual(Aluno.objects.count(), 1)
