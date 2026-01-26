# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2026-01-26 00:26:42

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 289
- **总 Thread 数**: 27
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 25 threads (269 邮件)
- **Other**: 2 threads (20 邮件)

---

## 📌 PATCH

共 25 个 thread

---

### Thread 1: [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 68 | **👥 参与者**: 9 | **📅 开始时间**: Mon, 12 Jan 2026 16:58:27 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM 架构的 MPAM（内存带宽分配管理）和 resctrl（资源控制）相关的补丁集（PATCH v3 00/47）。该补丁主要目的是为 KVM/arm64 添加 MPAM 的支持以及 resctrl 的集成代码。

在历史讨论中，补丁的背景主要涉及 MPAM 的实现细节，包括如何在上下文切换时管理 MPAM 寄存器、如何在 CPU 上线时重新初始化 MPAM 寄存器，以及如何为任务或 CPU 设置 MPAM 的 PARTID 和 PMG 值等。参与者们讨论了补丁的设计选择和潜在问题，并提出了代码审查意见。

本周的新讨论中，Gavin Shan 提供了对多个补丁的测试反馈，并确认在其测试平台上 L3 缓存分区和 MBW（软限制）功能正常。此外，参与者们继续讨论了补丁的细节，包括对代码风格的建议、潜在的错误修复和功能依赖关系的确认。Ben Horgan 对参与者的反馈表示感谢，并承诺将根据讨论结果更新补丁。

总体来看，讨论集中在确保补丁的功能完整性和代码质量上，参与者们积极提出建议和改进意见，以推动补丁的最终合并。

#### 📝 邮件列表

1. **[01-12 16:58]** [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[01-12 16:58]** [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[01-12 16:58]** [PATCH v3 07/47] arm64: mpam: Re-initialise MPAM regs when CPU comes online
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[01-12 16:58]** [PATCH v3 08/47] arm64: mpam: Advertise the CPUs MPAM limits to the driver
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[01-12 16:58]** [PATCH v3 09/47] arm64: mpam: Add cpu_pm notifier to restore MPAM sysregs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[01-12 16:58]** [PATCH v3 10/47] arm64: mpam: Initialise and context switch the MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[01-12 16:58]** [PATCH v3 11/47] arm64: mpam: Add helpers to change a task or cpu's MPAM PARTID/PMG values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[01-12 16:58]** [PATCH v3 14/47] arm_mpam: resctrl: Add boilerplate cpuhp and domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[01-12 16:58]** [PATCH v3 27/47] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[01-12 16:58]** [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[01-12 16:58]** [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
12. **[01-12 16:58]** [PATCH v3 30/47] arm_mpam: resctrl: Pre-allocate free running monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
13. **[01-12 16:58]** [PATCH v3 31/47] arm_mpam: resctrl: Pre-allocate assignable monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[01-12 16:59]** [PATCH v3 43/47] arm_mpam: Add quirk framework
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[01-12 16:59]** [PATCH v3 44/47] arm_mpam: Add workaround for T241-MPAM-1
   - 发件人: Ben Horgan <ben.horgan@arm.com>
16. **[01-12 16:59]** [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[01-12 16:59]** [PATCH v3 47/47] arm_mpam: Quirk CMN-650's CSU NRDY behaviour
   - 发件人: Ben Horgan <ben.horgan@arm.com>
18. **[01-13 08:49]** Re: [PATCH v3 14/47] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
19. **[01-13 15:14]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
20. **[01-15 14:47]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Gavin Shan <gshan@redhat.com>
21. **[01-15 12:09]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Jonathan Cameron <jonathan.cameron@huawei.com>
22. **[01-15 15:43]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[01-15 16:49]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Peter Newman <peternewman@google.com>
24. **[01-15 17:58]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
25. **[01-15 18:14]** Re: [PATCH v3 07/47] arm64: mpam: Re-initialise MPAM regs when CPU
 comes online
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
26. **[01-15 10:54]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
27. **[01-15 19:08]** Re: [PATCH v3 10/47] arm64: mpam: Initialise and context switch the
 MPAMSM_EL1 register
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
28. **[01-15 19:13]** Re: [PATCH v3 11/47] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
29. **[01-15 15:20]** Re: [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Fenghua Yu <fenghuay@nvidia.com>
30. **[01-16 10:29]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
31. **[01-16 10:34]** Re: [PATCH v3 31/47] arm_mpam: resctrl: Pre-allocate assignable
 monitors
   - 发件人: Shaopeng Tan (Fujitsu) <tan.shaopeng@fujitsu.com>
32. **[01-16 11:04]** Re: [PATCH v3 31/47] arm_mpam: resctrl: Pre-allocate assignable
 monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
33. **[01-19 09:30]** Re: [PATCH v3 00/47] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Gavin Shan <gshan@redhat.com>
34. **[01-19 14:37]** Re: [PATCH v3 08/47] arm64: mpam: Advertise the CPUs MPAM limits to
 the driver
   - 发件人: Gavin Shan <gshan@redhat.com>
35. **[01-19 14:40]** Re: [PATCH v3 09/47] arm64: mpam: Add cpu_pm notifier to restore MPAM
 sysregs
   - 发件人: Gavin Shan <gshan@redhat.com>
36. **[01-19 14:50]** Re: [PATCH v3 09/47] arm64: mpam: Add cpu_pm notifier to restore MPAM
 sysregs
   - 发件人: Gavin Shan <gshan@redhat.com>
37. **[01-19 14:51]** Re: [PATCH v3 10/47] arm64: mpam: Initialise and context switch the
 MPAMSM_EL1 register
   - 发件人: Gavin Shan <gshan@redhat.com>
38. **[01-19 14:56]** Re: [PATCH v3 11/47] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Gavin Shan <gshan@redhat.com>
39. **[01-19 15:01]** Re: [PATCH v3 11/47] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Gavin Shan <gshan@redhat.com>
40. **[01-19 19:53]** Re: [PATCH v3 27/47] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Gavin Shan <gshan@redhat.com>
41. **[01-19 19:57]** Re: [PATCH v3 30/47] arm_mpam: resctrl: Pre-allocate free running
 monitors
   - 发件人: Gavin Shan <gshan@redhat.com>
42. **[01-19 12:04]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm
 counters
   - 发件人: James Morse <james.morse@arm.com>
43. **[01-19 20:14]** Re: [PATCH v3 43/47] arm_mpam: Add quirk framework
   - 发件人: Gavin Shan <gshan@redhat.com>
44. **[01-19 20:16]** Re: [PATCH v3 44/47] arm_mpam: Add workaround for T241-MPAM-1
   - 发件人: Gavin Shan <gshan@redhat.com>
45. **[01-19 20:18]** Re: [PATCH v3 47/47] arm_mpam: Quirk CMN-650's CSU NRDY behaviour
   - 发件人: Gavin Shan <gshan@redhat.com>
46. **[01-19 12:23]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
47. **[01-19 13:47]** Re: [PATCH v3 29/47] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Peter Newman <peternewman@google.com>
48. **[01-19 13:38]** Re: [PATCH v3 07/47] arm64: mpam: Re-initialise MPAM regs when CPU
 comes online
   - 发件人: Ben Horgan <ben.horgan@arm.com>
49. **[01-19 13:40]** Re: [PATCH v3 10/47] arm64: mpam: Initialise and context switch the
 MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
50. **[01-19 13:53]** Re: [PATCH v3 27/47] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
51. **[01-19 14:00]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
52. **[01-19 14:22]** Re: [PATCH v3 07/47] arm64: mpam: Re-initialise MPAM regs when CPU
 comes online
   - 发件人: Ben Horgan <ben.horgan@arm.com>
53. **[01-19 14:49]** Re: [PATCH v3 08/47] arm64: mpam: Advertise the CPUs MPAM limits to
 the driver
   - 发件人: Ben Horgan <ben.horgan@arm.com>
54. **[01-19 15:08]** Re: [PATCH v3 09/47] arm64: mpam: Add cpu_pm notifier to restore MPAM
 sysregs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
55. **[01-19 15:31]** Re: [PATCH v3 10/47] arm64: mpam: Initialise and context switch the
 MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
56. **[01-19 15:47]** Re: [PATCH v3 11/47] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
57. **[01-19 15:49]** Re: [PATCH v3 11/47] arm64: mpam: Add helpers to change a task or
 cpu's MPAM PARTID/PMG values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
58. **[01-19 17:20]** Re: [PATCH v3 14/47] arm_mpam: resctrl: Add boilerplate cpuhp and
 domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
59. **[01-19 20:27]** Re: [PATCH v3 30/47] arm_mpam: resctrl: Pre-allocate free running
 monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
60. **[01-19 20:34]** Re: [PATCH v3 31/47] arm_mpam: resctrl: Pre-allocate assignable
 monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
61. **[01-19 20:48]** Re: [PATCH v3 43/47] arm_mpam: Add quirk framework
   - 发件人: Ben Horgan <ben.horgan@arm.com>
62. **[01-19 20:54]** Re: [PATCH v3 44/47] arm_mpam: Add workaround for T241-MPAM-1
   - 发件人: Ben Horgan <ben.horgan@arm.com>
63. **[01-19 20:56]** Re: [PATCH v3 45/47] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
64. **[01-19 20:58]** Re: [PATCH v3 47/47] arm_mpam: Quirk CMN-650's CSU NRDY behaviour
   - 发件人: Ben Horgan <ben.horgan@arm.com>
65. **[01-20 09:42]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Gavin Shan <gshan@redhat.com>
66. **[01-20 16:28]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Peter Newman <peternewman@google.com>
67. **[01-21 09:58]** Re: [PATCH v3 28/47] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Reinette Chatre <reinette.chatre@intel.com>
68. **[01-23 14:29]** Re: [PATCH v3 06/47] arm64: mpam: Context switch the MPAM registers
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>

---

### Thread 2: [PATCH v2 00/35] KVM: arm64: Add support for protected guest memory with pKVM

**📧 邮件数**: 36 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 19 Jan 2026 12:45:53 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上实现受保护虚拟机（pKVM）支持的多个补丁（patch）。以下是对讨论内容的总结：

1. **原始补丁内容**：本次补丁系列的核心是为 arm64 的 KVM 添加对受保护来宾内存的支持，允许虚拟机在隔离的环境中运行，增强安全性。补丁包括多个功能的实现，如内存捐赠、共享和回收机制。

2. **历史讨论要点**：之前的讨论主要集中在如何有效地管理受保护虚拟机的内存，包括如何处理内存的捐赠和回收，以及如何确保在不同虚拟机之间的内存隔离。参与者对补丁的设计和实现提出了反馈和建议，强调了内存管理的复杂性和潜在的安全隐患。

3. **本周的新讨论与进展**：本周的讨论中，Will Deacon 提出了多个补丁，涵盖了以下内容：
   - 引入新的超调用（hypercall）以支持受保护虚拟机的内存共享和取消共享。
   - 实现了对受保护虚拟机的内存强制回收机制，确保在内存被回收后，无法再次捐赠。
   - 增强了自测试功能，以验证内存捐赠和回收的正确性。
   - 添加了文档，帮助用户理解 pKVM 的功能和限制。

总的来说，本周的讨论和补丁推进了 pKVM 的功能实现，确保了受保护虚拟机在内存管理方面的安全性和有效性。

#### 📝 邮件列表

1. **[01-19 12:45]** [PATCH v2 00/35] KVM: arm64: Add support for protected guest memory with pKVM
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-19 12:45]** [PATCH v2 01/35] KVM: arm64: Invert KVM_PGTABLE_WALK_HANDLE_FAULT to fix pKVM walkers
   - 发件人: Will Deacon <will@kernel.org>
3. **[01-19 12:45]** [PATCH v2 02/35] KVM: arm64: Don't leak stage-2 page-table if VM fails to init under pKVM
   - 发件人: Will Deacon <will@kernel.org>
4. **[01-19 12:45]** [PATCH v2 03/35] KVM: arm64: Move handle check into pkvm_pgtable_stage2_destroy_range()
   - 发件人: Will Deacon <will@kernel.org>
5. **[01-19 12:45]** [PATCH v2 04/35] KVM: arm64: Rename __pkvm_pgtable_stage2_unmap()
   - 发件人: Will Deacon <will@kernel.org>
6. **[01-19 12:45]** [PATCH v2 05/35] KVM: arm64: Don't advertise unsupported features for protected guests
   - 发件人: Will Deacon <will@kernel.org>
7. **[01-19 12:45]** [PATCH v2 06/35] KVM: arm64: Expose self-hosted debug regs as RAZ/WI for protected guests
   - 发件人: Will Deacon <will@kernel.org>
8. **[01-19 12:46]** [PATCH v2 07/35] KVM: arm64: Remove is_protected_kvm_enabled() checks from hypercalls
   - 发件人: Will Deacon <will@kernel.org>
9. **[01-19 12:46]** [PATCH v2 08/35] KVM: arm64: Ignore MMU notifier callbacks for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
10. **[01-19 12:46]** [PATCH v2 09/35] KVM: arm64: Prevent unsupported memslot operations on protected VMs
   - 发件人: Will Deacon <will@kernel.org>
11. **[01-19 12:46]** [PATCH v2 10/35] KVM: arm64: Ignore -EAGAIN when mapping in pages for the pKVM host
   - 发件人: Will Deacon <will@kernel.org>
12. **[01-19 12:46]** [PATCH v2 11/35] KVM: arm64: Split teardown hypercall into two phases
   - 发件人: Will Deacon <will@kernel.org>
13. **[01-19 12:46]** [PATCH v2 12/35] KVM: arm64: Introduce __pkvm_host_donate_guest()
   - 发件人: Will Deacon <will@kernel.org>
14. **[01-19 12:46]** [PATCH v2 13/35] KVM: arm64: Hook up donation hypercall to pkvm_pgtable_stage2_map()
   - 发件人: Will Deacon <will@kernel.org>
15. **[01-19 12:46]** [PATCH v2 14/35] KVM: arm64: Handle aborts from protected VMs
   - 发件人: Will Deacon <will@kernel.org>
16. **[01-19 12:46]** [PATCH v2 15/35] KVM: arm64: Introduce __pkvm_reclaim_dying_guest_page()
   - 发件人: Will Deacon <will@kernel.org>
17. **[01-19 12:46]** [PATCH v2 16/35] KVM: arm64: Hook up reclaim hypercall to pkvm_pgtable_stage2_destroy()
   - 发件人: Will Deacon <will@kernel.org>
18. **[01-19 12:46]** [PATCH v2 17/35] KVM: arm64: Refactor enter_exception64()
   - 发件人: Will Deacon <will@kernel.org>
19. **[01-19 12:46]** [PATCH v2 18/35] KVM: arm64: Inject SIGSEGV on illegal accesses
   - 发件人: Will Deacon <will@kernel.org>
20. **[01-19 12:46]** [PATCH v2 19/35] KVM: arm64: Avoid pointless annotation when mapping host-owned pages
   - 发件人: Will Deacon <will@kernel.org>
21. **[01-19 12:46]** [PATCH v2 20/35] KVM: arm64: Generalise kvm_pgtable_stage2_set_owner()
   - 发件人: Will Deacon <will@kernel.org>
22. **[01-19 12:46]** [PATCH v2 21/35] KVM: arm64: Introduce host_stage2_set_owner_metadata_locked()
   - 发件人: Will Deacon <will@kernel.org>
23. **[01-19 12:46]** [PATCH v2 22/35] KVM: arm64: Change 'pkvm_handle_t' to u16
   - 发件人: Will Deacon <will@kernel.org>
24. **[01-19 12:46]** [PATCH v2 23/35] KVM: arm64: Annotate guest donations with handle and gfn in host stage-2
   - 发件人: Will Deacon <will@kernel.org>
25. **[01-19 12:46]** [PATCH v2 24/35] KVM: arm64: Introduce hypercall to force reclaim of a protected page
   - 发件人: Will Deacon <will@kernel.org>
26. **[01-19 12:46]** [PATCH v2 25/35] KVM: arm64: Reclaim faulting page from pKVM in spurious fault handler
   - 发件人: Will Deacon <will@kernel.org>
27. **[01-19 12:46]** [PATCH v2 26/35] KVM: arm64: Return -EFAULT from VCPU_RUN on access to a poisoned pte
   - 发件人: Will Deacon <will@kernel.org>
28. **[01-19 12:46]** [PATCH v2 27/35] KVM: arm64: Add hvc handler at EL2 for hypercalls from protected VMs
   - 发件人: Will Deacon <will@kernel.org>
29. **[01-19 12:46]** [PATCH v2 28/35] KVM: arm64: Implement the MEM_SHARE hypercall for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
30. **[01-19 12:46]** [PATCH v2 29/35] KVM: arm64: Implement the MEM_UNSHARE hypercall for protected VMs
   - 发件人: Will Deacon <will@kernel.org>
31. **[01-19 12:46]** [PATCH v2 30/35] KVM: arm64: Allow userspace to create protected VMs when pKVM is enabled
   - 发件人: Will Deacon <will@kernel.org>
32. **[01-19 12:46]** [PATCH v2 31/35] KVM: arm64: Add some initial documentation for pKVM
   - 发件人: Will Deacon <will@kernel.org>
33. **[01-19 12:46]** [PATCH v2 32/35] KVM: arm64: Extend pKVM page ownership selftests to cover guest donation
   - 发件人: Will Deacon <will@kernel.org>
34. **[01-19 12:46]** [PATCH v2 33/35] KVM: arm64: Register 'selftest_vm' in the VM table
   - 发件人: Will Deacon <will@kernel.org>
35. **[01-19 12:46]** [PATCH v2 34/35] KVM: arm64: Extend pKVM page ownership selftests to cover forced reclaim
   - 发件人: Will Deacon <will@kernel.org>
36. **[01-19 12:46]** [PATCH v2 35/35] KVM: arm64: Extend pKVM page ownership selftests to cover guest hvcs
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 3: [PATCH v9 00/13] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 23 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 14 Jan 2026 13:45:12 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v9 00/13] Direct Map Removal Support for guest_memfd”的补丁，旨在通过从主机内核的直接映射中解除虚拟机来宾内存的映射，以减轻Spectre等瞬态执行问题的影响。补丁中引入了一个新的标志GUEST_MEMFD_FLAG_NO_DIRECT_MAP，允许在创建guest_memfd时将其从直接映射中移除。

在历史讨论中，参与者们探讨了补丁的实现细节及其潜在影响，特别是如何处理直接映射的恢复以及与TDX（可信数据扩展）相关的特定问题。讨论中提到，直接映射的移除可能会影响性能，且需要确保在TDX虚拟机中不会导致崩溃。

本周的新讨论主要集中在补丁的进一步细化和潜在问题上。参与者们讨论了是否可以在特定情况下禁用直接映射的移除功能，尤其是在TDX系统中。Ackerley Tng提到，虽然目前没有明确的用例需要解除TDX私有内存的直接映射，但建议先阻止这一选项的使用，以简化后续的实现和测试过程。整体来看，参与者们对补丁的方向表示支持，但仍需解决一些技术细节和潜在的兼容性问题。

#### 📝 邮件列表

1. **[01-14 13:45]** [PATCH v9 00/13] Direct Map Removal Support for guest_memfd
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
2. **[01-14 13:45]** [PATCH v9 02/13] mm/gup: drop secretmem optimization from
 gup_fast_folio_allowed
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
3. **[01-14 13:46]** [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
4. **[01-15 12:00]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
5. **[01-15 13:40]** Re: [PATCH v9 02/13] mm/gup: drop secretmem optimization from gup_fast_folio_allowed
   - 发件人: Ackerley Tng <ackerleytng@google.com>
6. **[01-15 23:04]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
7. **[01-16 00:00]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
8. **[01-16 14:55]** Re: [PATCH v9 02/13] mm/gup: drop secretmem optimization from
 gup_fast_folio_allowed
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
9. **[01-16 14:56]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
10. **[01-16 15:00]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
11. **[01-16 09:30]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Vishal Annapurve <vannapurve@google.com>
12. **[01-16 17:51]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
13. **[01-21 16:20]** Re: [PATCH v9 02/13] mm/gup: drop secretmem optimization from gup_fast_folio_allowed
   - 发件人: Ackerley Tng <ackerleytng@google.com>
14. **[01-22 08:34]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
15. **[01-22 08:44]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
16. **[01-22 17:35]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>
17. **[01-22 18:04]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
18. **[01-22 10:37]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
19. **[01-22 18:47]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
20. **[01-22 12:30]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
21. **[01-22 20:40]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Nikita Kalyazin <kalyazin@amazon.com>
22. **[01-22 14:47]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Ackerley Tng <ackerleytng@google.com>
23. **[01-23 00:01]** Re: [PATCH v9 07/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Edgecombe, Rick P <rick.p.edgecombe@intel.com>

---

### Thread 4: [PATCH 0/6] KVM: arm64: ... and FWB for all

**📧 邮件数**: 20 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 19 Jan 2026 10:56:45 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 KVM（内核虚拟机）在 arm64 架构下的内存属性管理，特别是引入 FWB（Full Write Buffering）机制的相关补丁。

1. **原始补丁内容**：Marc Zyngier 提出了一个包含六个补丁的系列，旨在改进 KVM 在 arm64 上的内存属性处理，特别是通过引入新的标志 KVM_PGTABLE_S2_AS_S1，使得 Stage-2 的内存属性可以直接使用 Stage-1 的属性。

2. **之前讨论要点**：在历史讨论中，Marc 解释了当前主机在受保护模式下的内存属性处理方式，以及为何需要特殊处理主机的内存属性。之前的讨论主要集中在如何有效地利用 FWB 来改善内存属性的组合。

3. **本周的新讨论与进展**：本周的讨论中，Marc 提交了多个补丁，并得到了参与者的积极反馈和测试结果。Joey Gouly 和 Fuad Tabba 等人对补丁进行了审核并表示支持。Will Deacon 提出了对某些补丁的简化建议，而 Marc 也对一些补丁进行了调整和解释，强调了使用统一的属性编码方案的好处。整体来看，补丁系列得到了广泛的认可，预计将进一步推动 KVM 的改进。

#### 📝 邮件列表

1. **[01-19 10:56]** [PATCH 0/6] KVM: arm64: ... and FWB for all
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-19 10:56]** [PATCH 1/6] arm64: Add MT_S2{,_FWB}_AS_S1 encodings
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-19 10:56]** [PATCH 2/6] KVM: arm64: Add KVM_PGTABLE_S2_AS_S1 flag
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-19 10:56]** [PATCH 3/6] KVM: arm64: Make stage2_pte_cacheable() return false when S2_AS_S1 is set
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[01-19 10:56]** [PATCH 4/6] KVM: arm64: Switch pKVM host S2 over to KVM_PGTABLE_S2_AS_S1
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-19 10:56]** [PATCH 5/6] KVM: arm64: Kill KVM_PGTABLE_S2_NOFWB
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[01-19 10:56]** [PATCH 6/6] KVM: arm64: Simplify PAGE_S2_MEMATTR
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[01-21 16:23]** Re: [PATCH 0/6] KVM: arm64: ... and FWB for all
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[01-21 18:13]** Re: [PATCH 0/6] KVM: arm64: ... and FWB for all
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[01-22 15:03]** Re: [PATCH 6/6] KVM: arm64: Simplify PAGE_S2_MEMATTR
   - 发件人: Will Deacon <will@kernel.org>
11. **[01-22 15:04]** Re: [PATCH 3/6] KVM: arm64: Make stage2_pte_cacheable() return false
 when S2_AS_S1 is set
   - 发件人: Will Deacon <will@kernel.org>
12. **[01-22 15:07]** Re: [PATCH 1/6] arm64: Add MT_S2{,_FWB}_AS_S1 encodings
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[01-22 15:08]** Re: [PATCH 2/6] KVM: arm64: Add KVM_PGTABLE_S2_AS_S1 flag
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[01-22 15:09]** Re: [PATCH 5/6] KVM: arm64: Kill KVM_PGTABLE_S2_NOFWB
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[01-22 15:09]** Re: [PATCH 4/6] KVM: arm64: Switch pKVM host S2 over to KVM_PGTABLE_S2_AS_S1
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[01-22 17:05]** Re: [PATCH 2/6] KVM: arm64: Add KVM_PGTABLE_S2_AS_S1 flag
   - 发件人: Will Deacon <will@kernel.org>
17. **[01-23 12:22]** Re: [PATCH 0/6] KVM: arm64: ... and FWB for all
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
18. **[01-23 12:37]** Re: [PATCH 0/6] KVM: arm64: ... and FWB for all
   - 发件人: Marc Zyngier <maz@kernel.org>
19. **[01-23 13:21]** Re: [PATCH 3/6] KVM: arm64: Make stage2_pte_cacheable() return false when S2_AS_S1 is set
   - 发件人: Marc Zyngier <maz@kernel.org>
20. **[01-23 15:17]** Re: [PATCH 0/6] KVM: arm64: ... and FWB for all
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 5: [PATCH v2 0/5] KVM: arm64: Enforce MTE disablement at EL2

**📧 邮件数**: 14 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 20 Jan 2026 09:05:18 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下强制禁用 MTE（Memory Tagging Extension）的补丁系列，共包含五个补丁。补丁的主要目的是在 EL2（异常级别 2）中确保 MTE 被禁用，以提高系统的安全性和稳定性。

在历史讨论中，补丁的背景和目的已被阐明，但具体的历史讨论内容未被列出，因此我们无法提供详细的历史讨论要点。

在本周的新讨论中，参与者们针对补丁进行了多次回复和讨论。Fuad Tabba 提出是否需要将补丁重基于 6.19-rc6 版本。Marc Zyngier 对补丁的实现提出了改进建议，特别是在处理寄存器访问的灵活性方面。他认为当前的实现可能不够可扩展，建议使用更灵活的抽象方法。此外，Leonardo Bras 也参与了讨论，表示希望在新优化中使用该补丁集的功能。

最终，Marc Zyngier 确认了补丁的应用，并表示已经将其应用到下一个版本中。补丁系列的具体提交包括添加新的内存类型编码、引入新的 KVM 标志、切换 pKVM 主机的 S2 到新的标志、删除不再使用的标志，以及简化内存属性的处理。

#### 📝 邮件列表

1. **[01-20 09:05]** Re: [PATCH v2 0/5] KVM: arm64: Enforce MTE disablement at EL2
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[01-20 14:57]** Re: [PATCH v2 3/5] KVM: arm64: Refactor enter_exception64()
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-20 15:11]** Re: [PATCH v2 2/5] arm64: Clear HCR_EL2.ATA when MTE is not supported or disabled
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-22 15:12]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Leonardo Bras <leo.bras@arm.com>
5. **[01-22 15:16]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Leonardo Bras <leo.bras@arm.com>
6. **[01-23 10:15]** Re: [PATCH v2 1/5] arm64/sysreg: Add HDBSS related register information
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[01-23 19:16]** [PATCH v2 0/5] ... and FWB for all
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[01-23 19:16]** [PATCH v2 1/5] arm64: Add MT_S2{,_FWB}_AS_S1 encodings
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[01-23 19:16]** [PATCH v2 2/5] KVM: arm64: Add KVM_PGTABLE_S2_AS_S1 flag
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[01-23 19:16]** [PATCH v2 3/5] KVM: arm64: Switch pKVM host S2 over to KVM_PGTABLE_S2_AS_S1
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[01-23 19:16]** [PATCH v2 4/5] KVM: arm64: Kill KVM_PGTABLE_S2_NOFWB
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[01-23 19:16]** [PATCH v2 5/5] KVM: arm64: Simplify PAGE_S2_MEMATTR
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[01-25 13:50]** Re: [PATCH v2 3/5] KVM: arm64: Switch pKVM host S2 over to KVM_PGTABLE_S2_AS_S1
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[01-25 16:19]** Re: [PATCH v2 0/5] ... and FWB for all
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 6: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.

**📧 邮件数**: 14 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 19 Jan 2026 15:34:07 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH v11 RESEND 9/9），该补丁旨在为 SWPx 模拟应用 FEAT_LSUI 特性。补丁的主要内容是探讨在 SWPx 模拟中引入 LSUI 是否合适。

在历史讨论中，参与者们没有提供具体的历史背景，但本周的新讨论围绕该补丁的有效性展开。Yeoreum Yun 表示，虽然目前没有实际的 CPU 实现 LSUI，但他认为未来的 CPU 可能会同时支持 LSUI 和 32 位 EL0 兼容性，因此在 SWPx 模拟中应用 LSUI 是有意义的。然而，他也承认目前没有强烈的意见来支持或反对该补丁的应用。

本周的讨论进展显示，Yeoreum Yun 最终倾向于支持放弃该补丁，认为在当前情况下，LSUI 和 AArch32 兼容性可能不会同时存在，因此不需要在 SWPx 模拟中应用 LSUI。此外，Will Deacon 提出，如果 LSUI 和 AArch32 同时存在，可能会引发安全问题，建议在检测到 LSUI 时将 SWP 模拟状态设置为不可用。

综上所述，参与者们对补丁的有效性和必要性进行了深入讨论，最终达成共识，认为在当前情况下放弃该补丁是更为合理的选择。

#### 📝 邮件列表

1. **[01-19 15:34]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-19 22:32]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[01-20 09:32]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[01-20 09:46]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[01-20 10:07]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[01-20 11:50]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Will Deacon <will@kernel.org>
7. **[01-20 12:14]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[01-20 17:59]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[01-21 13:56]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Will Deacon <will@kernel.org>
10. **[01-21 14:51]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
11. **[01-21 16:20]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Will Deacon <will@kernel.org>
12. **[01-21 16:31]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
13. **[01-21 16:36]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Will Deacon <will@kernel.org>
14. **[01-21 16:51]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 7: [PATCH kvmtool v5 0/7] arm64: Nested virtualization support

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 23 Jan 2026 14:27:22 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的补丁系列（PATCH kvmtool v5 0/7）。该补丁系列的主要目标是增强 KVM 工具对 ARM64 嵌套虚拟化的支持。

**补丁内容**：
1. **补丁概述**：补丁系列的第一个补丁更新了内核头文件，以支持新的 EL2 能力，并设置维护 IRQ。后续补丁引入了新的命令行选项“--nested”，允许 VCPU 在 EL2 中启动，并增加了对 VGIC 的支持，以便 KVM 客户机能够在嵌套环境中运行。

**历史讨论要点**：
- 之前的讨论主要集中在如何实现嵌套虚拟化的各个方面，包括 IRQ 设置、计时器支持和命令行选项的设计。
- 参与者对补丁进行了审查和反馈，确保功能的正确性和兼容性。

**本周新讨论与进展**：
- 本周的讨论中，Andre Przywara 提到补丁修复了在某些维护 IRQ 设置失败时的边界情况，并增加了警告信息以防止错误使用命令行选项。
- Marc Zyngier 提出了对计数器偏移控制的支持，允许用户在创建虚拟机时设置该值。
- 讨论还涉及了对 FEAT_E2H0 的支持，允许在不强制 VHE 支持的情况下启动客户机。
- 最后，针对 virtio 的字节序处理进行了修复，以确保在 EL2 客户机中正确处理。

整体来看，这一系列补丁的实施将显著提升 ARM64 嵌套虚拟化的功能和稳定性。

#### 📝 邮件列表

1. **[01-23 14:27]** [PATCH kvmtool v5 0/7] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[01-23 14:27]** [PATCH kvmtool v5 1/7] Sync kernel UAPI headers with v6.19-rc6
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[01-23 14:27]** [PATCH kvmtool v5 2/7] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[01-23 14:27]** [PATCH kvmtool v5 3/7] arm64: nested: Add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[01-23 14:27]** [PATCH kvmtool v5 4/7] arm64: Add counter offset control
   - 发件人: Andre Przywara <andre.przywara@arm.com>
6. **[01-23 14:27]** [PATCH kvmtool v5 5/7] arm64: Add FEAT_E2H0 support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
7. **[01-23 14:27]** [PATCH kvmtool v5 6/7] arm64: Generate HYP timer interrupt specifiers
   - 发件人: Andre Przywara <andre.przywara@arm.com>
8. **[01-23 14:27]** [PATCH kvmtool v5 7/7] arm64: Handle virtio endianness reset when running nested
   - 发件人: Andre Przywara <andre.przywara@arm.com>
9. **[01-23 16:03]** Re: [PATCH kvmtool v5 7/7] arm64: Handle virtio endianness reset when running nested
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v8 RESEND 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 19 Jan 2026 10:29:21 +0800

#### 🤖 AI 总结

本邮件讨论的主题是为 Armv8.7 架构添加对 FEAT_{LS64, LS64_V} 的支持及相关测试。该功能引入了单拷贝原子 64 字节加载和存储指令，旨在提高用户空间驱动程序的性能，特别是在直接与硬件交互时。

在历史讨论中，参与者们讨论了如何在内核中识别和启用这些新特性，并将其暴露给用户空间。主要的讨论点包括如何处理不支持的内存访问，以及如何在虚拟机中正确处理这些指令的陷阱。

本周的新讨论中，Zhou Wang 提交了七个补丁，主要内容包括：
1. **补丁 1-6**：实现了对 FEAT_{LS64, LS64_V} 的支持，包括在用户空间中处理 LD64B 和 ST64B 指令的退出、文档更新、对不支持内存的 DABT 处理、EL2 的基本设置等。
2. **补丁 7**：增加了 HWCAP 测试，确保在支持这些特性的系统上，相关指令能够正常执行而不产生 SIGILL 信号。

最终，这些补丁得到了 Will Deacon 的认可并被应用到 arm64 的代码库中，标志着对该特性的支持已进入下一个阶段。

#### 📝 邮件列表

1. **[01-19 10:29]** [PATCH v8 RESEND 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[01-19 10:29]** [PATCH v8 RESEND 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B* outside of memslots
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
3. **[01-19 10:29]** [PATCH v8 RESEND 2/7] KVM: arm64: Add documentation for KVM_EXIT_ARM_LDST64B
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
4. **[01-19 10:29]** [PATCH v8 RESEND 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
5. **[01-19 10:29]** [PATCH v8 RESEND 4/7] arm64: Provide basic EL2 setup for FEAT_{LS64, LS64_V} usage at EL0/1
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
6. **[01-19 10:29]** [PATCH v8 RESEND 5/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the supported guest
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
7. **[01-19 10:29]** [PATCH v8 RESEND 6/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
8. **[01-19 10:29]** [PATCH v8 RESEND 7/7] kselftest/arm64: Add HWCAP test for FEAT_LS64
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
9. **[01-22 16:59]** Re: [PATCH v8 RESEND 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 9: [PATCH 0/3] arm64: Unconditionally compile LSE/PAN/EPAN support

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  7 Jan 2026 18:06:58 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构中无条件编译 LSE、PAN 和 EPAN 支持的补丁。历史讨论中，Marc Zyngier 提出了三个补丁，分别是无条件启用 LSE、PAN 和 EPAN 支持。他指出，LSE 和 PAN 自 ARMv8.1 发布以来已经存在很长时间，启用这些特性可以显著提高性能和安全性，而 EPAN 则是对 PAN 的有益补充。

在之前的讨论中，Marc 强调了这三个特性的必要性，并提到在现代设备中几乎都支持这些特性，因此建议将其默认启用。Will Deacon 对 EPAN 的启用表示了一些保留，认为在性能测试中可能会有些开销，建议可以再等几年再启用。

在本周的新讨论中，Will 确认已将前两个补丁（LSE 和 PAN）应用到 arm64 的开发分支中，并表示将处理与 KVM 相关的补丁冲突。Marc 也提到了一些相关的更改正在通过 KVM 树提交，确保与其他补丁的兼容性。整体来看，LSE 和 PAN 的补丁已获得通过，而 EPAN 的启用则暂时搁置。

#### 📝 邮件列表

1. **[01-07 18:06]** [PATCH 0/3] arm64: Unconditionally compile LSE/PAN/EPAN support
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-07 18:07]** [PATCH 2/3] arm64: Unconditionally enable PAN support
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-07 18:07]** [PATCH 3/3] arm64: Unconditionally enable EPAN support
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-22 10:15]** Re: [PATCH 3/3] arm64: Unconditionally enable EPAN support
   - 发件人: Will Deacon <will@kernel.org>
5. **[01-22 11:06]** Re: [PATCH 3/3] arm64: Unconditionally enable EPAN support
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-22 11:21]** Re: [PATCH 2/3] arm64: Unconditionally enable PAN support
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[01-22 16:59]** Re: [PATCH 0/3] arm64: Unconditionally compile LSE/PAN/EPAN support
   - 发件人: Will Deacon <will@kernel.org>
8. **[01-22 17:02]** Re: [PATCH 2/3] arm64: Unconditionally enable PAN support
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 10: [PATCH v12 0/7] support FEAT_LSUI

**📧 邮件数**: 8 | **👥 参与者**: 1 | **📅 开始时间**: Wed, 21 Jan 2026 19:06:15 +0000

#### 🤖 AI 总结

本邮件线程讨论了支持 Arm 架构中的 FEAT_LSUI 特性，主要涉及一系列补丁（PATCH v12 0/7），旨在改进内核对用户内存的访问方式。FEAT_LSUI 允许特权级别的代码在不清除 PSTATE.PAN 位的情况下访问用户内存，从而简化了内存操作。

在历史讨论中，补丁经历了多次重构和改进，逐步增加了对 FEAT_LSUI 的支持，包括对 futex 原子操作的重构和用户空间交换（user_swpX）仿真。补丁的更新记录显示，开发者在每个版本中都进行了细致的调整，以确保兼容性和功能的完整性。

本周的新讨论中，Yeoreum Yun 提交了七个补丁，具体内容包括：
1. 在 Kconfig 中添加对 LSUI 的支持。
2. 在 CPU 特性检测中加入 FEAT_LSUI。
3. 将 FEAT_LSUI 公开给 KVM 客户端。
4. 为 FEAT_LSUI 添加自测覆盖。
5. 重构 futex 原子操作以支持 FEAT_LSUI。
6. 在 futex 中实现使用 FEAT_LSUI 的操作。
7. 禁用 SWP 指令的仿真，以消除 PAN 切换。

这些补丁的实施将显著提升 Arm 架构在内核中的用户内存访问效率，并减少对传统方法的依赖。整体来看，讨论进展顺利，补丁得到了积极的反馈和审查。

#### 📝 邮件列表

1. **[01-21 19:06]** [PATCH v12 0/7] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[01-21 19:06]** [PATCH v12 1/7] arm64: Kconfig: add support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[01-21 19:06]** [PATCH v12 2/7] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[01-21 19:06]** [PATCH v12 3/7] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[01-21 19:06]** [PATCH v12 4/7] KVM: arm64: kselftest: set_id_regs: add test for FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[01-21 19:06]** [PATCH v12 5/7] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[01-21 19:06]** [PATCH v12 6/7] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[01-21 19:06]** [PATCH v12 7/7] arm64: armv8_deprecated: disable swp emulation when FEAT_LSUI present
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 11: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold
 ir_list_lock across IRTE updates in IOMMU)

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 08 Jan 2026 22:28:29 +0100

#### 🤖 AI 总结

本邮件线程讨论了由于调用 `irq_set_thread_affinity()` 可能导致的死锁问题，背景是与 KVM（内核虚拟机）相关的补丁（PATCH v3 38/62），该补丁旨在在 IOMMU 中更新 IRTE 时持有 `ir_list_lock` 锁。

在历史讨论中，Thomas Gleixner 和 Paolo Bonzini 提出了对该问题的不同看法。Gleixner 指出，内核中存在多个锁链问题，并质疑将其视为内核或中断（irq）错误的合理性。他强调，虽然这种锁的使用可能不优雅，但并不能简单地归结为错误。

在本周的新讨论中，Paolo Bonzini 提出了可能的解决方案，建议通过延迟调用 `irq_set_affinity()` 来避免死锁，特别是在 ARM64 架构的 KVM 中。他提到可以缓存处理器 ID，并在必要时发出请求以延迟加载。Marc Zyngier 也表示可能需要对 KVM 及其底层代码进行一些调整。Gleixner 进一步支持了延迟唤醒的建议，认为这是一个可行的解决方案。

总的来说，讨论围绕如何优雅地处理锁的使用及其对系统稳定性的影响展开，参与者们正在积极寻找解决方案以避免潜在的死锁问题。

#### 📝 邮件列表

1. **[01-08 22:28]** Re: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold
 ir_list_lock across IRTE updates in IOMMU)
   - 发件人: Thomas Gleixner <tglx@kernel.org>
2. **[01-08 22:53]** Re: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold
 ir_list_lock across IRTE updates in IOMMU)
   - 发件人: Thomas Gleixner <tglx@kernel.org>
3. **[01-21 16:53]** Re: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock
 across IRTE updates in IOMMU)
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
4. **[01-21 19:13]** Re: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock
 across IRTE updates in IOMMU)
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>
5. **[01-22 10:19]** Re: possible deadlock due to irq_set_thread_affinity() calling into the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across IRTE updates in IOMMU)
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-22 19:47]** Re: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold
 ir_list_lock across IRTE updates in IOMMU)
   - 发件人: Thomas Gleixner <tglx@kernel.org>
7. **[01-24 08:49]** Re: possible deadlock due to irq_set_thread_affinity() calling into
 the scheduler (was Re: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock
 across IRTE updates in IOMMU)
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

### Thread 12: [PATCH v9 25/30] KVM: arm64: Sync boot clock with the nVHE/pKVM hyp

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 07 Jan 2026 14:23:16 +0000

#### 🤖 AI 总结

在本邮件线程中，讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，特别是与 nVHE/pKVM hypervisor 相关的启动时钟同步问题。原始补丁（PATCH v9 25/30）旨在同步启动时钟，以提高虚拟化性能。

在历史讨论中，Marc Zyngier 提出了对补丁中将 X1 设置为 0 的必要性表示疑问，并建议是否可以重用已有的定义，尤其是在该补丁并非 EL2 代码的情况下。此外，他还指出了跟踪信息缺乏上下文的问题。

本周的新讨论中，Vincent Donnefort 和 Marc Zyngier 继续探讨了补丁的细节。Vincent 提到可以在事件头中添加与当前加载的 vCPU 相关的虚拟机进程 ID，以便于跟踪。Marc 进一步建议，应该使用线程名称来增强跟踪信息的可读性，以便更好地与 hypervisor 的跟踪输出进行关联。最终，双方达成共识，认为增加线程 PID 的信息是有益的。

总体来看，本周的讨论集中在如何增强补丁的跟踪能力和信息的可用性上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[01-07 14:23]** Re: [PATCH v9 25/30] KVM: arm64: Sync boot clock with the nVHE/pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-07 15:40]** Re: [PATCH v9 29/30] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-23 12:12]** Re: [PATCH v9 25/30] KVM: arm64: Sync boot clock with the nVHE/pKVM
 hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
4. **[01-23 12:14]** Re: [PATCH v9 29/30] KVM: arm64: Add selftest event support to
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
5. **[01-23 12:21]** Re: [PATCH v9 29/30] KVM: arm64: Add selftest event support to
 nVHE/pKVM hyp
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[01-23 12:47]** Re: [PATCH v9 29/30] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[01-23 12:47]** Re: [PATCH v9 29/30] KVM: arm64: Add selftest event support to nVHE/pKVM hyp
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v3 0/4] KVM: arm64: Enforce MTE disablement at EL2

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 22 Jan 2026 11:22:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中强制禁用 MTE（Memory Tagging Extension）功能的补丁。该补丁的目的是确保即使在硬件支持 MTE 的情况下，恶意主机也无法利用 MTE 对虚拟机或虚拟化管理程序进行攻击。

在历史讨论中，补丁的背景是，虽然 pKVM 从未向受保护的客户机暴露 MTE，但如果主机内核禁用 MTE，硬件仍然可能允许低级别异常访问 MTE 指令。为此，补丁提出在 EL2（异常级别 2）显式禁用 MTE，确保 MTE 指令会被捕获到虚拟化管理程序。

本周的新讨论中，Fuad Tabba 提出了四个补丁：
1. 移除重置 HCR_EL2 的无效代码。
2. 当 MTE 被禁用时，捕获对 MTE 访问的请求。
3. 在 MTE 被禁用时，访问 MTE 系统寄存器时注入未定义指令异常。
4. 在 pKVM 的陷阱初始化中使用更全面的 MTE 支持检查函数 kvm_has_mte()。

Marc Zyngier 对补丁表示认可，并已将其应用到下一个版本中。这些补丁的实施将增强 KVM 的安全性，防止潜在的 MTE 攻击。

#### 📝 邮件列表

1. **[01-22 11:22]** [PATCH v3 0/4] KVM: arm64: Enforce MTE disablement at EL2
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[01-22 11:22]** [PATCH v3 1/4] KVM: arm64: Remove dead code resetting HCR_EL2 for pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[01-22 11:22]** [PATCH v3 2/4] KVM: arm64: Trap MTE access and discovery when MTE is disabled
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[01-22 11:22]** [PATCH v3 3/4] KVM: arm64: Inject UNDEF when accessing MTE sysregs
 with MTE disabled
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[01-22 11:22]** [PATCH v3 4/4] KVM: arm64: Use kvm_has_mte() in pKVM trap initialization
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[01-23 11:47]** Re: [PATCH v3 0/4] KVM: arm64: Enforce MTE disablement at EL2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH v4 0/3] KVM ARM64 pre_fault_memory

**📧 邮件数**: 6 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 13 Jan 2026 15:26:39 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM ARM64 的补丁系列，旨在为 KVM_PRE_FAULT_MEMORY 特性提供支持，该特性之前仅在 x86 上可用。此补丁的主要目的是减少执行过程中的 stage-2 故障数量，特别是在内存密集型应用的后复制迁移场景中，以降低延迟。

在历史讨论中，参与者 Jack Thomson 提出了补丁的初步实现，并讨论了如何处理 stage-2 故障逻辑。Marc Zyngier 对补丁提出了质疑，认为如果已经声明了该能力，却在后续阶段表示不支持是不合理的。他还指出，用户空间在这种情况下将无法继续前进，可能导致问题。经过多次讨论，双方达成共识，认为需要在运行时进行处理，以应对用户空间的潜在错误。

在本周的新讨论中，Jack Thomson 对 Marc 的反馈表示感谢，并承认自己对之前评论的理解有误。他表示将考虑更全面地支持预故障功能，并计划在下一版补丁中进行修订。整体来看，讨论集中在补丁的实现细节及其对用户空间的影响上，双方都在寻求最佳的解决方案。

#### 📝 邮件列表

1. **[01-13 15:26]** [PATCH v4 0/3] KVM ARM64 pre_fault_memory
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
2. **[01-13 15:26]** [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Jack Thomson <jackabt.amazon@gmail.com>
3. **[01-15 09:51]** Re: [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[01-16 14:33]** Re: [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>
5. **[01-18 10:29]** Re: [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[01-19 11:10]** Re: [PATCH v4 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>

---

### Thread 15: [PATCH v11 RESEND 6/9] arm64: futex: support futex with FEAT_LSUI

**📧 邮件数**: 5 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 19 Jan 2026 16:37:33 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁，主题为“支持具有 FEAT_LSUI 的 futex”。该补丁旨在增强 futex 的功能，以支持新的指令特性 LSUI。

在历史讨论中，参与者们对补丁的设计和实现提出了多项建议和疑问，主要集中在如何处理 CPU 特性、内存访问和代码结构等方面。例如，有人指出不应假设在 LSUI 下总是有 PAN 特性，并建议在特性初始化时进行实际测试。此外，讨论中还提到了一些代码细节，如是否需要更新旧值、是否可以使用 32 位的 get_user() 等。

本周的新讨论中，Yeoreum Yun 和 Will Deacon 继续深入探讨补丁的实现细节。Yeoreum Yun 表示将根据 Will 的建议调整补丁，去掉不必要的假设和前缀，并考虑将 LSUI 特性仅在非大端 CPU 上启用。Will 则建议重构 CAS 辅助函数，使其更清晰，并区分故障和比较失败的情况。最终，Yeoreum Yun 表示将根据讨论的反馈重新提交补丁。

总体来看，本周的讨论进一步明确了补丁的方向和实现细节，参与者们积极协作，推动了补丁的完善。

#### 📝 邮件列表

1. **[01-19 16:37]** Re: [PATCH v11 RESEND 6/9] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-19 22:17]** Re: [PATCH v11 RESEND 6/9] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[01-20 15:44]** Re: [PATCH v11 RESEND 6/9] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[01-21 13:48]** Re: [PATCH v11 RESEND 6/9] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Will Deacon <will@kernel.org>
5. **[01-21 14:16]** Re: [PATCH v11 RESEND 6/9] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 16: [PATCH v5 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 21 Jan 2026 08:27:11 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是对 KVM（Kernel-based Virtual Machine）在 arm64 架构下支持 FF-A（Firmware Framework for Arm）直接消息接口的补丁。原始补丁包含两个部分，旨在实现对 FFA_MSG_SEND_DIRECT_REQ 和 FFA_MSG_SEND_DIRECT_REQ2 的支持。

在历史讨论中，之前的补丁版本（v4）因用例不明确而被删除，但现在已经明确了用例，即在内核启动时使用 TPM 设备与 CRB 通过 FF-A 进行通信。补丁的主要内容是允许主机处理直接消息，并过滤掉框架消息。

本周的新讨论中，Per Larsen 提交了补丁 v5，包含两部分：第一部分支持 FFA_MSG_SEND_DIRECT_REQ，第二部分支持 FFA_MSG_SEND_DIRECT_REQ2。补丁经过测试，能够在 QEMU 下成功启动 Android。然而，Will Deacon 对补丁提出了批评，指出 'vm_handle' 变量的使用并未达到预期效果，建议检查 FF-A 规范中编码的发送者 ID，而不是使用本地变量。Will 还强调了在邮件列表上进行技术讨论的重要性，以减少反复的审查周期。

总的来说，本周的讨论集中在补丁的实现细节及其有效性上，特别是对消息发送者 ID 的验证提出了改进建议。

#### 📝 邮件列表

1. **[01-21 08:27]** [PATCH v5 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[01-21 08:27]** [PATCH v5 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[01-21 08:27]** [PATCH v5 2/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[01-23 12:55]** Re: [PATCH v5 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in
 host handler
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 17: [PATCH kvmtool v4 3/7] arm64: nested: Add support for setting
 maintenance IRQ

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 16 Jan 2026 18:10:11 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 工具的补丁，主题为“为 arm64 嵌套添加设置维护 IRQ 的支持”。该补丁的目的是解决在使用 GICv3 时，如果没有设置维护 IRQ 的能力，可能会导致嵌套功能出现问题。

在历史讨论中，Sascha Bischoff 提出了一个问题，认为如果属性不存在，应该返回错误，同时指出即使无法设置维护 IRQ，仍然会生成相应的设备树属性，这可能导致不必要的混淆。

在本周的新讨论中，Marc Zyngier 和 Andre Przywara 对补丁进行了进一步的讨论和修改。Sascha Bischoff 确认了需要修复的问题，并感谢 Andre 的努力。Andre 提到已经修改代码，使得在 HAS 调用或 SET 调用失败时返回错误，这样可以自动解决问题，因为设备树的添加依赖于嵌套功能的支持。如果内核不支持该设备属性，则嵌套功能会失败。最终，Sascha 对这些修改表示满意，并确认在捕获 HAS 调用失败后，补丁的逻辑是合理的。

总体而言，本周的讨论集中在对补丁的修正和确认上，确保了在处理 GICv3 和 GICv5 时的兼容性和正确性。

#### 📝 邮件列表

1. **[01-16 18:10]** Re: [PATCH kvmtool v4 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[01-19 09:13]** Re: [PATCH kvmtool v4 3/7] arm64: nested: Add support for setting maintenance IRQ
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-22 15:54]** Re: [PATCH kvmtool v4 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[01-22 16:45]** Re: [PATCH kvmtool v4 3/7] arm64: nested: Add support for setting
 maintenance IRQ
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 18: [PATCH v4 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 09 Jan 2026 22:34:24 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下对 FF-A（Firmware Framework for Arm）直接消息接口的支持，主要包含两个补丁。

**原始补丁内容**：
第一个补丁（PATCH v4 0/2）旨在无条件支持 FFA_MSG_SEND_DIRECT_REQ，并在超管协商版本为 1.2 及以上时支持 FFA_MSG_SEND_DIRECT_REQ2。补丁中指出，FF-A 控制平面中的框架消息将被过滤，且 REQ2 接口的消息始终为分区消息。第二个补丁（PATCH v4 1/2）则允许从主机转发直接消息，确保主机不发送框架消息。

**之前讨论要点**：
在历史讨论中，Per Larsen 提出需要验证发送者是否为 HOST_FFA_ID，但此部分在后续讨论中被认为不再需要，因为现在只需检查标志位是否为零。

**本周的新讨论与进展**：
本周的讨论中，Will Deacon 提出了对补丁的反馈，确认了不再需要对 HOST_FFA_ID 的验证。Eric Auger 则分享了他在迁移过程中成功测试了与 PSCI 版本相关的功能，表示可以从支持 PSCI v1.2 和 v1.3 的主机迁移到不支持的旧主机，进一步验证了补丁的有效性。

总体来看，讨论围绕补丁的实现细节和验证过程展开，参与者对补丁的有效性和必要性进行了积极的交流。

#### 📝 邮件列表

1. **[01-09 22:34]** [PATCH v4 0/2] KVM: arm64: Support FF-A direct messaging
 interfaces
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[01-09 22:34]** [PATCH v4 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in host
 handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[01-20 14:10]** Re: [PATCH v4 1/2] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ in
 host handler
   - 发件人: Will Deacon <will@kernel.org>
4. **[01-21 10:39]** Re: [PATCH v4 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Eric Auger <eric.auger@redhat.com>

---

### Thread 19: [PATCH] KVM: arm64: nv: Return correct RES0 bits for FGT registers

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 21 Jan 2026 18:16:31 +0800

#### 🤖 AI 总结

本邮件主题为“[PATCH] KVM: arm64: nv: Return correct RES0 bits for FGT registers”，主要讨论了对 KVM 中 arm64 架构下 FGT 寄存器的修复。

原始 patch 的内容是修正 `kvm_get_sysreg_res0()` 函数，以确保其返回 FGT 寄存器的正确 RES0 位。此修复是基于之前的提交（commit a0162020095e），扩展了系统寄存器的掩码基础设施，使其不再局限于 VNCR-backed 寄存器。具体来说，修复了寄存器索引转换中的错误，确保返回正确的 RES0 位。

在之前的讨论中，Zenghui Yu 指出，当前代码中存在一些不必要的条件判断，建议将其移除。Marc Zyngier 也对此表示赞同，并指出在多个地方进行寄存器索引到数组索引的转换是一个潜在的错误，建议进行统一处理。

本周的新讨论中，Zenghui Yu 提交了修复补丁，并得到了 Marc Zyngier 的认可，Marc 表示已将该补丁应用到下一个版本中，并感谢 Zenghui 的贡献。这表明该问题得到了及时解决，并将改善 KVM 的稳定性和性能。

#### 📝 邮件列表

1. **[01-21 18:16]** [PATCH] KVM: arm64: nv: Return correct RES0 bits for FGT registers
   - 发件人: Zenghui Yu <zenghui.yu@linux.dev>
2. **[01-22 09:07]** Re: [PATCH] KVM: arm64: nv: Return correct RES0 bits for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-22 09:11]** Re: [PATCH] KVM: arm64: nv: Return correct RES0 bits for FGT registers
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 20: [PATCH v2 4/6] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 20 Jan 2026 14:15:58 -0700

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中处理 RES1 位的补丁（PATCH v2 4/6）。该补丁的目的是在 DECLARE_FEAT_MAP() 函数中考虑 RES1 位，以确保特性映射的准确性。

在历史讨论中，虽然没有具体的邮件记录，但补丁引入后，参与者 Nathan Chancellor 报告了在其两台 arm64 设备上出现的多个“未定义行为”错误。这些错误与 RES1 位的处理有关，导致特性映射与实际硬件不匹配。

本周的新讨论中，Nathan 提出了问题的具体表现，Marc Zyngier 解释了问题的根源，指出由于对某些旧款 ARM CPU（如 Cortex-A72）的优化，跳过了 FGT（Fine-Grained Trapping）陷阱表的解析，导致 RES1 位的处理不当。Marc 认为这种优化并不值得保留，并提出了一种新的解决方案，确保在不支持 FGT 的硬件上仍能进行有效检查。经过测试，Nathan 确认在应用新补丁后，未再出现警告，表示该解决方案有效。

总结来说，本周的讨论集中在补丁引发的问题及其解决方案上，参与者们达成了一致，认为新方案能够有效解决 RES1 位处理中的错误。

#### 📝 邮件列表

1. **[01-20 14:15]** Re: [PATCH v2 4/6] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Nathan Chancellor <nathan@kernel.org>
2. **[01-21 10:50]** Re: [PATCH v2 4/6] KVM: arm64: Account for RES1 bits in DECLARE_FEAT_MAP() and co
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[01-21 16:32]** Re: [PATCH v2 4/6] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Nathan Chancellor <nathan@kernel.org>

---

### Thread 21: [PATCH v11 RESEND 4/9] arm64: Kconfig: Detect toolchain support
 for LSUI

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 19 Jan 2026 15:50:43 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的 Kconfig patch，旨在检测工具链对 LSUI（不特权加载存储指令）的支持。该 patch 的主要内容是新增一个 Kconfig 选项，以便在编译时能够识别是否支持 LSUI。

在之前的讨论中，参与者们提到该 Kconfig 变量是内部使用的，因此建议去掉帮助文本。Will Deacon 强调，尽管可以去掉帮助文本，但保留有关支持的编译器信息作为注释是有益的，这样可以与其他工具链特性测试保持一致。

本周的新讨论中，Yeoreum Yun 提出了更新的 patch 版本，包含了对 ARMv9.6 架构特性的菜单配置，并详细描述了 LSUI 的功能及其对编译器的支持要求（LLVM 20+ 和 binutils 2.45+）。参与者们对该更新进行了讨论，进一步明确了 Kconfig 的配置和注释内容。整体来看，讨论集中在如何优化 Kconfig 的描述和确保信息的准确性上。

#### 📝 邮件列表

1. **[01-19 15:50]** Re: [PATCH v11 RESEND 4/9] arm64: Kconfig: Detect toolchain support
 for LSUI
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-19 15:54]** Re: [PATCH v11 RESEND 4/9] arm64: Kconfig: Detect toolchain support
 for LSUI
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[01-20 11:35]** Re: [PATCH v11 RESEND 4/9] arm64: Kconfig: Detect toolchain support
 for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 22: [PATCH v12 06/46] arm64: RMI: Define the user ABI

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 23 Jan 2026 16:47:06 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个名为“[PATCH v12 06/46] arm64: RMI: Define the user ABI”的补丁，该补丁旨在定义 ARM64 架构下的用户应用程序接口（ABI）。补丁的主要内容是为 RMI（Resource Management Interface）提供一个用户可用的接口定义，以便在虚拟化环境中更好地管理资源。

在历史讨论中，参与者们探讨了如何将这些 ABI 变更与相应的实现补丁分开，以便更全面地理解这些用户接口在整体架构中的作用。此外，讨论中提到了一些调用限制，例如 `source_uaddr` 应该与共享模式下的“DRAM”位于不同的内存区域，以及在将整个访客内存转换为私有之前是否可以调用这些接口。

在本周的新讨论中，Suzuki K Poulose 提出了将变更拆分的建议，并询问了关于调用限制的具体细节，特别是关于在将 DRAM 转换为私有内存后的调用时机。Alper Gun 则关注于用户空间接口的简化，询问了关于 rpv 和 hash_algo 配置的未来可能性。整体来看，讨论集中在补丁的实现细节和用户接口的可用性上。

#### 📝 邮件列表

1. **[01-23 16:47]** Re: [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
2. **[01-23 10:57]** Re: [PATCH v12 22/46] arm64: RMI: Create the realm descriptor
   - 发件人: Alper Gun <alpergun@google.com>

---

### Thread 23: [PATCH] KVM: arm64: Always populate FGT masks at boot time

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 22 Jan 2026 08:51:53 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在确保在启动时始终填充 FGT（Fine Grained Traps）掩码。

**原始补丁内容**：补丁的主要目的是在启动时无条件地生成 FGT 掩码，而不仅仅在硬件支持 FEAT_FGT 的情况下进行。这是因为在缺乏 FGT 支持的情况下，仍然会检查特定功能的位分配，导致启动时产生大量无关的警告。通过始终填充 FGT 掩码，可以减少这些警告并确保检查的有效性。

**之前的讨论要点**：在历史讨论中，补丁的背景是由于引入 RES1 支持后，系统寄存器的处理变得更加复杂，导致了启动时的噪声问题。补丁的提出是为了优化这一过程，并减少不必要的内存占用。

**本周的新讨论与进展**：本周的讨论中，Marc Zyngier 确认该补丁已被应用，并感谢参与者的贡献。这表明补丁已经成功整合到下一步的开发中，解决了之前提到的问题。

#### 📝 邮件列表

1. **[01-22 08:51]** [PATCH] KVM: arm64: Always populate FGT masks at boot time
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[01-22 09:11]** Re: [PATCH] KVM: arm64: Always populate FGT masks at boot time
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 24: [PATCH v11 RESEND 5/9] arm64: futex: refactor futex atomic
 operation

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 19 Jan 2026 15:57:16 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARM64 架构下 futex 原子操作的重构，具体的补丁为 "[PATCH v11 RESEND 5/9] arm64: futex: refactor futex atomic operation"。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁旨在优化和重构现有的 futex 原子操作代码，以提高其可读性和性能。

在本周的新讨论中，参与者 Will Deacon 提出了一个建议，认为在重构代码的同时，可以考虑使用命名参数来替代数字参数，以增强代码的可读性。对此，Yeoreum Yun 表示赞同，并表示将尝试实现这一建议。

总结而言，本周的讨论集中在如何进一步改善补丁的实现上，特别是通过使用命名参数来提升代码的清晰度。

#### 📝 邮件列表

1. **[01-19 15:57]** Re: [PATCH v11 RESEND 5/9] arm64: futex: refactor futex atomic
 operation
   - 发件人: Will Deacon <will@kernel.org>
2. **[01-19 22:19]** Re: [PATCH v11 RESEND 5/9] arm64: futex: refactor futex atomic
 operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 25: [PATCH kvmtool v4 5/7] arm64: Add FEAT_E2H0 support

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 16 Jan 2026 18:12:40 +0000

#### 🤖 AI 总结

在本邮件线程中，讨论的主题是关于一个针对 KVM 工具的补丁，内容为在 arm64 架构中添加 FEAT_E2H0 支持。该补丁的目的是增强 KVM 工具的功能，使其能够更好地处理嵌套虚拟化。

在历史讨论中，参与者 Andre Przywara 提出了补丁，并得到了 Sascha Bischoff 的审核认可。Sascha 提到，FEAT_E2H0 选项只有在启用嵌套虚拟化（--nested）时才会被使用，因此建议在仅提供 --e2h0 选项时，打印出该选项被忽略的警告，以避免用户产生误解。

在本周的新讨论中，Marc Zyngier 对 Sascha 的建议表示赞同，并确认将添加一个警告，指明在未启用嵌套虚拟化时，--e2h0 选项将被忽略。这一进展有助于提升用户体验，确保用户对选项的使用有清晰的理解。

#### 📝 邮件列表

1. **[01-16 18:12]** Re: [PATCH kvmtool v4 5/7] arm64: Add FEAT_E2H0 support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[01-19 09:38]** Re: [PATCH kvmtool v4 5/7] arm64: Add FEAT_E2H0 support
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v6 00/14] arm64: EL2 support

**📧 邮件数**: 18 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 23 Jan 2026 16:50:39 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 单元测试的 EL2 支持，包含一系列补丁（PATCH v6 00/14），旨在增强在 EL2 环境下运行测试的能力。

**原始问题**：本次补丁系列的目标是为 KVM 单元测试添加对 EL2 的支持，主要包括修复在 EL2 下运行时的各种问题，如 GIC 初始化溢出、定时器中断处理等。

**历史讨论要点**：之前的讨论集中在如何确保在 EL2 下的环境设置正确，以及如何处理与 GIC 相关的错误。补丁中提到的微基准测试失败，原因是 GICv3 的 redistributor 未正确初始化。

**本周新进展**：本周的讨论中，Joey Gouly 提出了多个补丁，修复了 GIC 初始化、定时器 IRQ 处理、以及在 EL2 下的测试执行方式等问题。此外，增加了对 EL2 环境变量的支持，并在 CI 中添加了 EL2 测试。尽管大部分补丁得到了认可，但仍有一个定时器测试在 EL2 下超时，导致需要进一步调查。Andrew Jones 建议暂时从 CI 中移除该测试，以便进行深入分析。

总体来看，该系列补丁为 KVM 在 ARM64 的 EL2 支持奠定了基础，但仍需解决定时器测试中的问题。

#### 📝 邮件列表

1. **[01-23 16:50]** [kvm-unit-tests PATCH v6 00/14] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[01-23 16:50]** [kvm-unit-tests PATCH v6 01/14] arm64: fix overflow in gic-v2 initialisation
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[01-23 16:50]** [kvm-unit-tests PATCH v6 02/14] arm64: set SCTLR_EL1 to a known value for secondary cores
   - 发件人: Joey Gouly <joey.gouly@arm.com>
4. **[01-23 16:50]** [kvm-unit-tests PATCH v6 03/14] arm64: drop to EL1 if booted at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
5. **[01-23 16:50]** [kvm-unit-tests PATCH v6 04/14] arm64: efi: initialise SCTLR_ELx fully
   - 发件人: Joey Gouly <joey.gouly@arm.com>
6. **[01-23 16:50]** [kvm-unit-tests PATCH v6 05/14] arm64: efi: initialise the EL
   - 发件人: Joey Gouly <joey.gouly@arm.com>
7. **[01-23 16:50]** [kvm-unit-tests PATCH v6 06/14] arm64: timer: use hypervisor timers when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
8. **[01-23 16:50]** [kvm-unit-tests PATCH v6 07/14] arm64: micro-bench: fix timer IRQ
   - 发件人: Joey Gouly <joey.gouly@arm.com>
9. **[01-23 16:50]** [kvm-unit-tests PATCH v6 08/14] arm64: micro-bench: use smc when at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
10. **[01-23 16:50]** [kvm-unit-tests PATCH v6 09/14] arm64: selftest: update test for running at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
11. **[01-23 16:50]** [kvm-unit-tests PATCH v6 10/14] arm64: pmu: count EL2 cycles
   - 发件人: Joey Gouly <joey.gouly@arm.com>
12. **[01-23 16:50]** [kvm-unit-tests PATCH v6 11/14] arm64: run at EL2 if supported
   - 发件人: Joey Gouly <joey.gouly@arm.com>
13. **[01-23 16:50]** [kvm-unit-tests PATCH v6 12/14] arm64: add EL2 environment variable
   - 发件人: Joey Gouly <joey.gouly@arm.com>
14. **[01-23 16:50]** [kvm-unit-tests PATCH v6 13/14] arm64: debug: skip tests at EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>
15. **[01-23 16:50]** [kvm-unit-tests PATCH v6 14/14] arm64: gitlab-ci: add EL2 tests to CI
   - 发件人: Joey Gouly <joey.gouly@arm.com>
16. **[01-23 13:23]** Re: [kvm-unit-tests PATCH v6 00/14] arm64: EL2 support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
17. **[01-23 19:30]** Re: [kvm-unit-tests PATCH v6 00/14] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
18. **[01-23 14:53]** Re: [kvm-unit-tests PATCH v6 00/14] arm64: EL2 support
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 2: KVM/arm64 fixes for 6.19

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 15 Jan 2026 01:30:25 -0800

#### 🤖 AI 总结

本邮件线程讨论了针对 Linux 内核 6.19 版本的 KVM/arm64 修复补丁。历史讨论中，Oliver Upton 提出了一个修复集，主要针对非标准配置下的问题，如 pKVM、hVHE 和嵌套虚拟化等。该补丁集的详细信息已在邮件中提供，并请求 Paolo 进行拉取。

在本周的新讨论中，Paolo Bonzini 确认已成功拉取 Oliver 提供的补丁，并表示他在等待其他架构的反馈，但目前看来情况相对平静，没有其他问题出现。

总结而言，本周的讨论没有新的问题或补丁提出，主要是对之前修复集的确认和状态更新。

#### 📝 邮件列表

1. **[01-15 01:30]** KVM/arm64 fixes for 6.19
   - 发件人: Oliver Upton <oupton@kernel.org>
2. **[01-24 08:46]** Re: KVM/arm64 fixes for 6.19
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

