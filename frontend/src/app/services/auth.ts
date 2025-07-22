import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { tap } from 'rxjs/operators';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class Auth {
  private apiUrl = `${environment.apiUrl}/auth`;
  private isLoggedIn = false;

  constructor(private http: HttpClient) {}

  // O método de login recebe as credenciais e faz a chamada HTTP
  login(credentials: { username: string; password: string }): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, credentials, { withCredentials: true }).pipe(
      // O tap "espia" a resposta de sucesso para atualizar o estado
      tap(() => this.setAuthenticated(true))
    );
  }

  logout(): Observable<any> {
    return this.http.post(`${this.apiUrl}/logout`, {}, { withCredentials: true }).pipe(
      tap(() => this.setAuthenticated(false))
    );
  }

  isAuthenticated(): boolean {
    return this.isLoggedIn;
  }

  setAuthenticated(status: boolean) {
    this.isLoggedIn = status;
  }
}