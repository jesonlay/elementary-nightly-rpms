Summary:        elementary GTK+ Stylesheet
Name:           egtk
Version:        5.0.0~rev%{rev}
Release:        2%{?dist}
License:        GPLv3
URL:            http://launchpad.net/egtk

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

BuildArch:      noarch

BuildRequires:  /usr/bin/install

Obsoletes:      egtk-common
Obsoletes:      egtk-gtk2-theme
Obsoletes:      egtk-gtk3-theme
Obsoletes:      egtk-metacity-theme
Obsoletes:      egtk-xfwm4-theme


%description
The official elementary GTK+ stylesheet designed to be smooth, attractive, fast, and usable.


%prep
%autosetup


%build


%install
mkdir -p %{buildroot}/%{_datadir}/themes/%{name}

install index.theme %{buildroot}/%{_datadir}/themes/%{name}/
install -d gtk-2.0 gtk-3.0 plank %{buildroot}/%{_datadir}/themes/%{name}/


%clean
rm -rf %{buildroot}


%files
%doc AUTHORS CONTRIBUTORS ELEMENTARYOS HACKING
%license COPYING

%{_datadir}/themes/egtk


%changelog
* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev660-2
- Update for packaging changes.

* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev%{rev}-1
- Initial package.


