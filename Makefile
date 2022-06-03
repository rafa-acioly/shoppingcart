run:
	@pipenv run python3 -m uvicorn shoppingcart.main:app --reload

test:
	@pipenv run python3 -m pytest
