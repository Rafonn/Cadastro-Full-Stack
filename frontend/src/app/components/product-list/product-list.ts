import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';

import { ProductService } from '../../services/product';
import { Auth } from '../../services/auth';
import { ProductModel } from '../../models/productModel';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.html',
  styleUrls: ['./product-list.css'],
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule]
})
export class ProductListComponent implements OnInit {
  products: ProductModel[] = [];
  productForm: FormGroup;
  editingProduct: ProductModel | null = null;

  constructor(
    private productService: ProductService,
    private fb: FormBuilder,
    private router: Router,
    private authService: Auth
  ) {
    this.productForm = this.fb.group({
      name: ['', Validators.required],
      brand: ['', Validators.required],
      value: ['', [Validators.required, Validators.min(0.01)]]
    });
  }

  ngOnInit(): void {
    this.loadProducts();
  }

  loadProducts(): void {
    this.productService.getProducts().subscribe(data => {
      this.products = data;
    });
  }

  onSubmit(): void {
    if (this.productForm.invalid) {
      return;
    }

    if (this.editingProduct) {
      // ATUALIZAÇÃO
      this.productService.updateProduct(this.editingProduct.id, this.productForm.value).subscribe(() => {
        this.loadProducts();
        this.resetForm();
      });
    } else {
      // CRIAÇÃO
      this.productService.createProduct(this.productForm.value).subscribe(() => {
        this.loadProducts();
        this.resetForm();
      });
    }
  }

  editProduct(product: ProductModel): void {
    this.editingProduct = product;
    // Preenche o formulário com os dados do produto para edição
    this.productForm.setValue({
      name: product.name,
      brand: product.brand,
      value: product.value
    });
  }

  deleteProduct(id: number): void {
    // Adiciona uma confirmação para segurança
    if (confirm('Tem certeza que deseja excluir este produto?')) {
      this.productService.deleteProduct(id).subscribe(() => {
        this.loadProducts();
      });
    }
  }

  resetForm(): void {
    this.editingProduct = null;
    this.productForm.reset();
  }

  logout(): void {
    this.authService.logout();

    this.router.navigate(['/login'])
  }
}