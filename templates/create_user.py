{% extends "block.html" %}
{% block page_content %}
    <div class="container">
		<div class="row">
			<div class="panel panel-primary">
				<div class="panel-body">
					<form method="POST" action="#" role="form">
						<div class="form-group">
							<h2>CREATE USER</h2>
						</div>
						<div class="form-group">
							<label class="control-label" for="Email">Email</label>
							<input id="email" type="email" maxlength="50" class="form-control">
						</div>
						<div class="form-group">
							<label class="control-label" for="Password">First Name</label>
							<input id="first_name" type="text" maxlength="25" class="form-control" length="40">
						</div>
						<div class="form-group">
							<label class="control-label" for="Password">Last Name</label>
							<input id="last_name" type="text" maxlength="25" class="form-control" length="40">
						</div>
						<div class="form-group">
							<label class="control-label" for="Password">Password</label>
							<input id="password" type="password" maxlength="25" class="form-control" length="40">
						</div>
						<div class="form-group">
							<label class="control-label" for="Password">Confirm Password</label>
							<input id="confirm_password" type="password" maxlength="25" class="form-control" length="40">
						</div>

						<div class="form-group">
							<button id="Submit" type="submit" class="btn btn-info btn-block">CREATE USER/button>
						</div>						
					</form>
				</div>
			</div>
		</div>
	</div>
{% endblock %}