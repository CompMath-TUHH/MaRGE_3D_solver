"""
List of parameters required for 3D MRE as solved according to Daitche's paper
"""

class DaitcheParameters:

  def set_beta(self):
    self.beta = self.rho_p /self.rho_f

  def set_S(self):
    self.S = (1.0/3.0)*self.a**2/(self.nu * self.T)

  def set_R(self):
    self.R = 3.0/(1.0 + 2.0*self.beta)

  def set_gravity(self):
    self.g = (self.T/self.U)*9.8

  def __init__(self, particle_density, fluid_density, particle_radius,
                     kinematic_viscosity, time_scale, char_vel):
    self.rho_p = particle_density
    self.rho_f = fluid_density
    self.a     = particle_radius
    self.nu    = kinematic_viscosity
    self.T     = time_scale
    self.U     = char_vel

    self.set_beta()
    self.set_S()
    self.set_R()
    self.set_gravity()