import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ProductModel } from '../models/productModel';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private apiUrl = `${environment.apiUrl}/products`;

  constructor(private http: HttpClient) { }

  // Adicione a opção aqui
  getProducts(): Observable<ProductModel[]> {
    return this.http.get<ProductModel[]>(this.apiUrl, { withCredentials: true });
  }

  // E aqui
  createProduct(ProductModel: Omit<ProductModel, 'id'>): Observable<ProductModel> {
    return this.http.post<ProductModel>(this.apiUrl, ProductModel, { withCredentials: true });
  }

  // E aqui
  updateProduct(id: number, ProductModel: Partial<ProductModel>): Observable<ProductModel> {
    return this.http.put<ProductModel>(`${this.apiUrl}/${id}`, ProductModel, { withCredentials: true });
  }

  // E finalmente aqui
  deleteProduct(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/${id}`, { withCredentials: true });
  }
}