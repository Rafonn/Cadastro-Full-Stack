import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withInterceptors } from '@angular/common/http'; // Importe 'withInterceptors'
import { routes } from './app.routes';
import { authInterceptor } from './interceptors/auth-interceptor'; // Importe seu interceptador

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(
      withInterceptors([authInterceptor]) // Registre o interceptador aqui
    )
  ]
};