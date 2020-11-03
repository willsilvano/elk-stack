package main

import (
	"fmt"
	"net/http"

	"go.elastic.co/apm/module/apmhttp"
)

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", HelloHandler)
	http.ListenAndServe(":8080", apmhttp.Wrap(mux))
}

func HelloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello World!")
}
