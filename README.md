# `AI Resume Backend API`

## Deskripsi Proyek

Proyek ini adalah backend (server) yang dirancang untuk mendukung aplikasi pembuat resume yang ditenagai oleh kecerdasan buatan (AI). Proyek ini bertanggung jawab untuk memproses data pengguna, berinteraksi dengan model AI untuk analisis dan pembuatan konten, serta menyediakan API yang terstruktur untuk komunikasi dengan frontend.

## Fitur Utama

-   **Pembuatan Konten Otomatis**: Memanfaatkan model AI untuk menghasilkan deskripsi pekerjaan, ringkasan profil, dan poin-poin prestasi yang relevan.
-   **API RESTful**: Menyediakan serangkaian endpoint API yang aman dan efisien untuk mengelola data resume.
-   **Validasi Data**: Memastikan data yang dikirim oleh pengguna sesuai dengan format yang dibutuhkan.
-   **Manajemen Resume**: Memungkinkan pengguna untuk menyimpan, memperbarui, dan menghapus resume mereka.

---

## Teknologi yang Digunakan

* **Bahasa Pemrograman**: Python
* **Framework**: FastAPI
* **Model AI**: Open AI
* **Database**: PostgreSQL
* **Alat Pengembangan**: Docker, UV

---

## Panduan Instalasi

Ikuti langkah-langkah di bawah ini untuk menjalankan proyek ini secara lokal.

### Prasyarat

-   [Python 3.10+](https://www.python.org/downloads/)
-   [UV](https://docs.astral.sh/uv/) (untuk manajemen dependensi)
-   [Docker](https://www.docker.com/) (opsional, untuk menjalankan database)
-   [PostgreSQL](https://www.postgresql.org/)

### Langkah-langkah

1.  **Clone repositori:**
    ```bash
    git clone [https://github.com/Abito21/ai-resume-backend.git](https://github.com/Abito21/ai-resume-backend.git)
    cd ai-resume-backend
    ```

2.  **Instal dependensi:**
    ```bash
    uv install
    ```

3.  **Konfigurasi Variabel Lingkungan:**
    Buat file `.env` di direktori root dan tambahkan konfigurasi berikut. Ganti nilai-nilai dalam `<...>` dengan informasi Anda.

    ```env
    # Database
    DB_USER=your_username
    DB_PASS=your_password
    DB_HOST=localhost
    DB_PORT=port
    DB_NAME=ai_resume_db
    ```

4.  **Jalankan Database (dengan Docker):**
    Jika Anda menggunakan Docker, Anda bisa menjalankan database dengan perintah berikut:
    ```bash
    docker-compose up -d db
    ```
    atau, jalankan secara manual jika Anda telah menginstalnya.

5.  **Jalankan Aplikasi:**
    ```bash
    uv run uvicorn main:app --reload
    ```
    Aplikasi sekarang akan berjalan di `http://127.0.0.1:8000`.

---

## Dokumentasi API

Proyek ini menggunakan **FastAPI**, yang secara otomatis menghasilkan dokumentasi API interaktif menggunakan **Swagger UI**. Setelah aplikasi berjalan, Anda dapat mengakses dokumentasi di:
`http://127.0.0.1:8000/docs`

Dokumentasi ini mencakup daftar endpoint yang tersedia, metode HTTP yang digunakan, format request/response, dan kemampuan untuk mencoba setiap endpoint secara langsung.

---
## Penjelasan API & Integrasi dengan Frontend

Proyek ini menyediakan API RESTful yang dapat diakses dari frontend (aplikasi web atau mobile) untuk mengelola data resume. Dokumentasi API interaktif tersedia di **`http://127.0.0.1:8000/docs`** setelah server berjalan.

### Cara Akses dari Frontend

Aplikasi frontend dapat berkomunikasi dengan backend melalui permintaan HTTP (GET, POST, PUT, DELETE) menggunakan pustaka seperti `fetch` atau `axios` di JavaScript. Berikut adalah contoh cara mengakses setiap endpoint:

#### 1. Membuat Resume Baru
-   **Endpoint**: `POST /api/v1/resumes/`
-   **Tujuan**: Mengirimkan data resume baru untuk disimpan.
-   **Contoh Kode**:
    ```javascript
    const resumeData = {
        "name": "Budi Santoso",
        "email": "budi@example.com",
        "experience": [{"title": "Software Engineer"}],
        // ... data lainnya
    };

    fetch('[http://127.0.0.1:8000/api/v1/resumes/](http://127.0.0.1:8000/api/v1/resumes/)', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(resumeData),
    })
    .then(response => response.json())
    .then(data => console.log('Resume berhasil dibuat:', data))
    .catch(error => console.error('Error:', error));
    ```

#### 2. Mendapatkan Semua Resume
-   **Endpoint**: `GET /api/v1/resumes/`
-   **Tujuan**: Mengambil daftar semua resume yang tersimpan.
-   **Contoh Kode**:
    ```javascript
    fetch('[http://127.0.0.1:8000/api/v1/resumes/](http://127.0.0.1:8000/api/v1/resumes/)')
        .then(response => response.json())
        .then(data => console.log('Daftar resume:', data))
        .catch(error => console.error('Error:', error));
    ```

#### 3. Mendapatkan Detail Resume
-   **Endpoint**: `GET /api/v1/resumes/{resume_id}`
-   **Tujuan**: Mengambil detail spesifik dari satu resume berdasarkan ID-nya.
-   **Contoh Kode**:
    ```javascript
    const resumeId = "123e4567-e89b-12d3-a456-426614174000"; // Contoh UUID
    fetch(`http://127.0.0.1:8000/api/v1/resumes/${resumeId}`)
        .then(response => response.json())
        .then(data => console.log('Detail resume:', data))
        .catch(error => console.error('Error:', error));
    ```

#### 4. Memperbarui Resume
-   **Endpoint**: `PUT /api/v1/resumes/{resume_id}`
-   **Tujuan**: Memperbarui data resume yang sudah ada.
-   **Contoh Kode**:
    ```javascript
    const resumeId = "123e4567-e89b-12d3-a456-426614174000";
    const updatedData = {"name": "Budi Santoso (Updated)"};

    fetch(`http://127.0.0.1:8000/api/v1/resumes/${resumeId}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(updatedData),
    })
    .then(response => response.json())
    .then(data => console.log('Resume berhasil diperbarui:', data))
    .catch(error => console.error('Error:', error));
    ```

#### 5. Menghapus Resume
-   **Endpoint**: `DELETE /api/v1/resumes/{resume_id}`
-   **Tujuan**: Menghapus resume dari database.
-   **Contoh Kode**:
    ```javascript
    const resumeId = "123e4567-e89b-12d3-a456-426614174000";
    fetch(`http://127.0.0.1:8000/api/v1/resumes/${resumeId}`, {
        method: 'DELETE',
    })
    .then(response => {
        if (response.ok) {
            console.log('Resume berhasil dihapus.');
        } else {
            console.error('Gagal menghapus resume.');
        }
    })
    .catch(error => console.error('Error:', error));
    ```

---