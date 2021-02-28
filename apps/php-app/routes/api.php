<?php

use App\Http\Controllers\StatusController;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('status', [StatusController::class, 'status']);
Route::get('test-error', [StatusController::class, 'testError']);
Route::post('test-post', [StatusController::class, 'testPost']);
Route::post('test-apm', [StatusController::class, 'testApm']);
