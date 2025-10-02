   from flask import redirect

   @app.route('/c')
   def fix_c():
       return redirect('/', code=302)

