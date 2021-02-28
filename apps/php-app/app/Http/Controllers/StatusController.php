<?php

namespace App\Http\Controllers;

use Exception;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Log;

class StatusController extends Controller
{
    public function status()
    {
        return response()->json(['success' => true]);
    }

    public function testError()
    {
        throw new Exception('ERROOOO!');
        return response()->json(['success' => false], 200);
    }

    public function testPost(Request $request)
    {
        return response()->json(['success' => true], 200);
    }

    public function testApm()
    {
    }
}
