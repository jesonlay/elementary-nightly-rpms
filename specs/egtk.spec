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
* Sun Aug 21 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev688-1
- Update to latest snapshot.

* Fri Aug 12 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev687-1
- Update to latest snapshot.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev686-1
- Update to latest snapshot.

* Mon Aug 08 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev685-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev683-2
- Update for packaging changes.

* Mon Aug 01 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev683-1
- Update to latest snapshot.

* Thu Jul 21 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev681-1
- Update to latest snapshot.

* Tue Jul 19 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev678-1
- Update to latest snapshot.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev677-2
- Update for packaging changes.

* Mon Jun 20 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev674-1
- Update to latest snapshot.

* Mon Jun 13 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev672-1
- Update to latest snapshot.

* Thu Jun 09 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev671-1
- Update to latest snapshot.

* Sun Jun 05 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev670-1
- Update to latest snapshot.

* Tue May 31 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev669-1
- Update to latest snapshot.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev668-2
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev668-1
- Update to latest snapshot.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev667-2
- Update for packaging changes.

* Mon May 23 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev667-1
- Update to latest snapshot.

* Fri May 20 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev666-1
- Update to latest snapshot.

* Wed May 18 2016 Fabio Valentini <decathorpe@gmail.com> - 5.0.0~rev665-1
- Update to latest snapshot.

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


