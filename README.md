# HTML-Python


## run server test

```bash
python server.py # python >= 3.80
```

then visit [http://127.0.0.1:8326](http://127.0.0.1:8326), will be return follow html code.

```html
<!DOCTYPE html>
<html lang="en">
    <head class="">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="this is website description">
        <meta name="keyword" content="this is website keyword">
        <title>this is test document</title>
        <style>
            .flex {
                display: flex;
            }

            .justify-around {
                justify-content: space-around;
            }

            .w-full {
                width: 100%;
            }

            .items-center {
                align-items: center;
            }

            .gap-2 {
                gap: 0.5rem;
            }

            .relative {
                position: relative;
            }

            .justify-center {
                justify-content: center;
            }

            .p-3 {
                padding: 0.75rem;
            }

            * {
                padding: 0;
                margin: 0;
            }
        </style>
    </head>
    <body>
        <div class="flex justify-around w-full items-center gap-2 relative" data-active="0" aria-label="tabs">
            <div class="flex justify-center items-center p-3 flex justify-center items-center p-3" aria-label="tab-item" data-status="active">home</div>
            <div class="flex justify-center items-center p-3 flex justify-center items-center p-3" aria-label="tab-item">project</div>
            <div class="flex justify-center items-center p-3 flex justify-center items-center p-3" aria-label="tab-item">photos</div>
        </div>
    </body>
</html>
```

you can switch tab via path:
```
http://localhost:8326/active/home
http://localhost:8326/active/project
http://localhost:8326/active/photos
```