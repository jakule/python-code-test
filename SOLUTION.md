Q&A
---

*We need to be able to import all existing Starships to the provided Starship Model*

`./manage.py import_ships`

*A potential buyer can browse all Starships*

`http://localhost:8008/starships/`

*A potential buyer can browse all the listings for a given starship_class*

Example: 

`http://localhost:8008/listings?ship_type__starship_class=Star dreadnought`

*A potential buyer can sort listings by price or time of listing*

`http://localhost:8008/listings?ordering=price`

`http://localhost:8008/listings?ordering=created`

*To list a Starship as for sale, the user should supply the Starship name and list price*

Example: 

`POST http://localhost:8008/listings/43/`

```json
{
	"ship_name": "abc",
	"price": 1020
}
```

*A seller can deactivate and reactivate their listing*

Example:

`PATCH http://localhost:8008/listings/43/`
```json
{
	"active": false
}
```
or activate with `"active": true`

Other
---

I migrated the project from `pip` to `pipenv`.
I formatted the code with `yapf` to be consistent and follow PEP8 rules.