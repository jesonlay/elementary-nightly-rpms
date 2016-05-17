Summary:        elementary GTK+ Stylesheet
Name:           egtk
Version:        5.0.0~rev%{rev}
Release:        1%{?dist}
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

cp -p index.theme %{buildroot}/%{_datadir}/themes/%{name}/
cp -pr gtk-2.0 %{buildroot}/%{_datadir}/themes/%{name}/
cp -pr gtk-3.0 %{buildroot}/%{_datadir}/themes/%{name}/
cp -pr plank %{buildroot}/%{_datadir}/themes/%{name}/


%clean
rm -rf %{buildroot}


%files
%doc AUTHORS CONTRIBUTORS ELEMENTARYOS HACKING
%license COPYING

%{_datadir}/themes/egtk


%changelog
* Tue May 17 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev664-1
- Update to latest snapshot.

* Wed May 11 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev662-1
- Update to latest snapshot.

* Fri May 06 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev661-1
- Update to latest snapshot.

* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev660-3
- Update for packaging changes.

* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev660-2
- Update for packaging changes.

* Thu May 05 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev%{rev}-1
- Initial package.


