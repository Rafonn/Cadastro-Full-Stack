import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';
import { Auth } from '../services/auth';

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  // Usamos inject() para pegar a instância do serviço dentro da função
  const authService = inject(Auth);
  const token = authService.getToken();

  if (token) {
    // Clona a requisição para adicionar o novo cabeçalho
    req = req.clone({
      setHeaders: {
        Authorization: `Bearer ${token}`
      }
    });
  }

  // Passa a requisição (original ou clonada) para o próximo handler
  return next(req);
};