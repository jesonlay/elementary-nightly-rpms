Summary:        Pantheon Shell metapackage
Name:           pantheon-shell
Version:        0.1
Release:        0%{?dist}
License:        GPLv2

BuildArch:      noarch

Requires:       cerbere
Requires:       gala
Requires:       pantheon-xsession-settings
Requires:       plank
Requires:       slingshot-launcher
Requires:       wingpanel


%description
This metapackage pulls in all pantheon shell components.


%prep


%build


%install


%clean
rm -rf %{buildroot}


%files


%changelog


