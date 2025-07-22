import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Auth } from '../../services/auth'; // Verifique se o nome do arquivo é auth.service.ts
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-login',
  templateUrl: './login.html',
  styleUrls: ['./login.css'],
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule] // Não precisa do HttpClientModule aqui
})
export class LoginComponent {
  loginForm: FormGroup;
  errorMessage: string = '';

  constructor(
    private fb: FormBuilder,
    private authService: Auth,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      username: ['admin', Validators.required], // Pode pré-preencher para facilitar o teste
      password: ['password123', Validators.required]
    });
  }

  // ...
  onSubmit(): void {
  if (this.loginForm.invalid) return;

  this.authService.login(this.loginForm.value).subscribe(response => {
    const token = response.token;
    localStorage.setItem('token', token);

    console.log('Token salvo:', token);

    this.router.navigate(['/products']).then(success => {
      console.log('Redirecionamento para /products:', success ? 'OK' : 'Falhou');
    });
  });
}
  // ...
}