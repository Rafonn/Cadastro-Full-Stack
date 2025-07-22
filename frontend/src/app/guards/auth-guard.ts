import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { Auth } from '../services/auth';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authService: Auth, private router: Router) {}

  canActivate(): boolean {
    if (this.authService.isAuthenticated()) {
      return true; // Usuário está logado, permite o acesso.
    } else {
      this.router.navigate(['/login']); // Usuário não está logado, redireciona.
      return false;
    }
  }
}