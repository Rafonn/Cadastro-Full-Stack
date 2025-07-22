import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ProductModel } from '../models/productModel';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = 'http://127.0.0.1:5000/api/products';

  constructor(private http: HttpClient) {}

  private getAuthHeaders(): HttpHeaders {
    const token = localStorage.getItem('token');
    return new HttpHeaders({
      Authorization: `Bearer ${token}`
    });
  }

  getProducts(): Observable<ProductModel[]> {
    return this.http.get<ProductModel[]>(this.apiUrl, {
      headers: this.getAuthHeaders()
    });
  }

  createProduct(product: Partial<ProductModel>): Observable<any> {
    return this.http.post(this.apiUrl, product, {
      headers: this.getAuthHeaders()
    });
  }

  updateProduct(id: number, product: Partial<ProductModel>): Observable<any> {
    return this.http.put(`${this.apiUrl}/${id}`, product, {
      headers: this.getAuthHeaders()
    });
  }

  deleteProduct(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`, {
      headers: this.getAuthHeaders()
    });
  }
}
