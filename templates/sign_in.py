{% extends "block.html" %}
{% block page_content %}
    <div class="container">
		<div class="row">
			<div class="panel panel-primary">
				<div class="panel-body">
					<form method="POST" action="#" role="form">
						<div class="form-group">
							<h2>SIGN IN</h2>
						</div>
						<div class="form-group">
							<label class="control-label" for="signupEmail">Email</label>
							<input id="email" type="email" maxlength="50" class="form-control" required>
						</div>
						<div class="form-group">
							<label class="control-label" for="signupPassword">Password</label>
							<input id="password" type="password" maxlength="25" class="form-control" length="40" required>
						</div>
						<div class="form-group">
							<button id="Submit" type="submit" class="btn btn-info btn-block">Sign IN</button>
						</div>						
					</form>
				</div>
			</div>
		</div>
	</div>
{% endblock %}